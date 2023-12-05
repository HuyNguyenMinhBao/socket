import socket
import base64
import tkinter as tk

class SendPage:
    def __init__(self, root):
        root.geometry("600x400")

        self.sender_email_var = tk.StringVar()
        # password_var = tk.StringVar()  # Uncomment if you want to use a password field
        self.receiver_email_var = tk.StringVar()
        self.subject_var = tk.StringVar()
        self.body_var = tk.StringVar()

        # Creating a label for sender email
        sender_email_label = tk.Label(root, text='From', font=('calibre', 10, 'bold'))

        # Creating an entry for sender email
        sender_email_entry = tk.Entry(root, textvariable=self.sender_email_var, font=('calibre', 10, 'bold'))

        # Creating a label for receiver email
        receiver_email_label = tk.Label(root, text='To', font=('calibre', 10, 'bold'))

        # Creating an entry for receiver email
        receiver_email_entry = tk.Entry(root, textvariable=self.receiver_email_var, font=('calibre', 10, 'bold'))

        # Creating a label for subject
        subject_label = tk.Label(root, text='Subject', font=('calibre', 10, 'bold'))

        # Creating an entry for subject
        subject_entry = tk.Entry(root, textvariable=self.subject_var, font=('calibre', 10, 'bold'))

        # Create send button
        send_button = tk.Button(root, text='Send', command=self.send_email)

        sender_email_label.grid(row=0, column=0)
        sender_email_entry.grid(row=0, column=1)
        receiver_email_label.grid(row=1, column=0)
        receiver_email_entry.grid(row=1, column=1)
        subject_label.grid(row=2, column=0)
        subject_entry.grid(row=2, column=1)
        send_button.grid(row=3, column=1)

    def send_email(self):
        # Get user input
        sender_email = self.sender_email_var.get()
        # password = password_var.get()
        receiver_email = self.receiver_email_var.get()
        subject = self.subject_var.get()

        print(f"From: {sender_email}")
        print(f"To: {receiver_email}")
        print(f"Subject: {subject}")

        # Email server information
        smtp_server = '127.0.0.1'
        smtp_port = 2225

        # Connect to the SMTP server
        s = socket.socket()
        s.connect((smtp_server, smtp_port))
        recv1 = s.recv(1024)
        print(recv1.decode())

        # Send EHLO to start the session
        s.sendall(b'EHLO example.com\r\n')
        recv1 = s.recv(1024)
        print(recv1.decode())

        # Send base64-encoded username
        s.sendall(base64.b64encode(sender_email.encode() + b'\r\n'))
        recv1 = s.recv(1024)
        print(recv1.decode())
        
        s.sendall(base64.b64encode(receiver_email.encode() + b'\r\n'))
        recv1 = s.recv(1024)
        print(recv1.decode())

        s.sendall(base64.b64encode(subject.encode() + b'\r\n'))
        recv1 = s.recv(1024)
        print(recv1.decode())

        # Send base64_encode password
        # s.sendall(base64.b64encode(password.encode() + b'\r\n'))
        # recv1 = s.recv(1024)
        # print(recv1.decode())

        # Compose the email
        email_message = f"From: {sender_email}\r\nTo: {receiver_email}\r\nSubject: {subject}\r\n\r\n"

        # Send the email
        s.sendall(email_message.encode())

if __name__ == '__main__':
    root = tk.Tk()
    send_page = SendPage(root)
    root.mainloop()
