# Introduction to Internet Protocols: HTTP, HTTPS, FTP, SMTP, IMAP, POP3, VoIP

import socket
import subprocess
import platform
import time

# Introduction to HTTP
def http_introduction():
    explanation = """
    HTTP (Hypertext Transfer Protocol) is the protocol used for transferring web pages on the internet. 
    It is an application layer protocol and works based on a client-server model, where a client (browser) sends requests
    and the server responds with the requested data (e.g., HTML, images).
    """
    return explanation

# Introduction to HTTPS
def https_introduction():
    explanation = """
    HTTPS (Hypertext Transfer Protocol Secure) is the secure version of HTTP. It uses SSL/TLS encryption to secure the communication
    between a web browser and a server. HTTPS ensures that data transmitted between the client and server is encrypted and secure.
    """
    return explanation

# Introduction to FTP
def ftp_introduction():
    explanation = """
    FTP (File Transfer Protocol) is a standard network protocol used for transferring files between a client and a server over a TCP/IP network.
    It works on a client-server model, where the client sends requests to the server to upload or download files.
    FTP uses port 21 for communication.
    """
    return explanation

# Introduction to SMTP
def smtp_introduction():
    explanation = """
    SMTP (Simple Mail Transfer Protocol) is used for sending emails between mail servers. 
    It is an application layer protocol that allows clients (email programs) to send outgoing mail to a mail server.
    SMTP operates on port 25 (though modern email services often use other ports like 587 for secure email transmission).
    """
    return explanation

# Introduction to IMAP
def imap_introduction():
    explanation = """
    IMAP (Internet Message Access Protocol) is used by email clients to retrieve emails from a mail server.
    Unlike POP3, IMAP allows for synchronization between multiple devices as the messages are stored on the server.
    It operates on port 143 by default and supports secure communication over port 993 (IMAPS).
    """
    return explanation

# Introduction to POP3
def pop3_introduction():
    explanation = """
    POP3 (Post Office Protocol version 3) is used for retrieving emails from a mail server. 
    Unlike IMAP, POP3 downloads emails to the client and removes them from the server, making the mail accessible offline.
    It operates on port 110 and uses port 995 for secure communication (POP3S).
    """
    return explanation

# Introduction to VoIP
def voip_introduction():
    explanation = """
    VoIP (Voice over Internet Protocol) is a technology that allows voice communication over the internet or IP networks. 
    It converts analog voice signals into digital data and transmits them over IP-based networks.
    Popular VoIP protocols include SIP (Session Initiation Protocol) and RTP (Real-Time Transport Protocol).
    """
    return explanation

# Simulating an HTTP request (Python's built-in HTTP server example)
def http_simulation():
    try:
        response = subprocess.check_output(["curl", "http://example.com"], universal_newlines=True)
        return response[:200]  # Returning first 200 characters of the response for brevity
    except subprocess.CalledProcessError as e:
        return f"HTTP request failed: {e}"

# Simulating an FTP connection (Using Python's ftplib)
def ftp_simulation():
    from ftplib import FTP
    try:
        ftp = FTP("ftp.dlptest.com")
        ftp.login()  # Logging into the FTP server (anonymous login)
        ftp.cwd("/")  # Changing to the root directory
        files = ftp.nlst()  # Listing files in the directory
        ftp.quit()
        return files[:5]  # Displaying the first 5 files for brevity
    except Exception as e:
        return f"FTP connection failed: {e}"

# Simulating an SMTP connection (Sending a test email via SMTP)
def smtp_simulation():
    import smtplib
    from email.mime.text import MIMEText

    try:
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        from_email = "your-email@gmail.com"  # Replace with your email
        to_email = "recipient-email@example.com"  # Replace with recipient's email
        subject = "Test Email"
        body = "This is a test email sent via SMTP."
        
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = from_email
        msg["To"] = to_email
        
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(from_email, "your-password")  # Use app-specific password for Gmail
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()
        return "Test email sent successfully."
    except Exception as e:
        return f"SMTP connection failed: {e}"

# Simulating an IMAP connection (Retrieving emails)
def imap_simulation():
    import imaplib
    try:
        imap_server = "imap.gmail.com"
        email_account = "your-email@gmail.com"  # Replace with your email
        password = "your-password"  # Use app-specific password for Gmail
        
        mail = imaplib.IMAP4_SSL(imap_server)
        mail.login(email_account, password)
        mail.select("inbox")
        status, messages = mail.search(None, "ALL")
        mail.logout()
        
        return f"Total messages: {len(messages[0].split())}"
    except Exception as e:
        return f"IMAP connection failed: {e}"

# Simulating a POP3 connection (Retrieving emails)
def pop3_simulation():
    import poplib
    try:
        pop3_server = "pop.gmail.com"
        email_account = "your-email@gmail.com"  # Replace with your email
        password = "your-password"  # Use app-specific password for Gmail
        
        pop_conn = poplib.POP3_SSL(pop3_server)
        pop_conn.user(email_account)
        pop_conn.pass_(password)
        num_messages = len(pop_conn.list()[1])
        pop_conn.quit()
        
        return f"Total messages: {num_messages}"
    except Exception as e:
        return f"POP3 connection failed: {e}"

# Running all protocols and their simulations
def run_all_protocols():
    print("Introduction to Internet Protocols\n")

    # HTTP Introduction and Simulation
    print("HTTP (Hypertext Transfer Protocol):")
    print(http_introduction())
    print("HTTP Request Simulation:")
    print(http_simulation(), "\n")

    # HTTPS Introduction
    print("HTTPS (Hypertext Transfer Protocol Secure):")
    print(https_introduction(), "\n")

    # FTP Introduction and Simulation
    print("FTP (File Transfer Protocol):")
    print(ftp_introduction())
    print("FTP File Listing Simulation:")
    print(ftp_simulation(), "\n")

    # SMTP Introduction and Simulation
    print("SMTP (Simple Mail Transfer Protocol):")
    print(smtp_introduction())
    print("SMTP Email Sending Simulation:")
    print(smtp_simulation(), "\n")

    # IMAP Introduction and Simulation
    print("IMAP (Internet Message Access Protocol):")
    print(imap_introduction())
    print("IMAP Email Retrieval Simulation:")
    print(imap_simulation(), "\n")

    # POP3 Introduction and Simulation
    print("POP3 (Post Office Protocol version 3):")
    print(pop3_introduction())
    print("POP3 Email Retrieval Simulation:")
    print(pop3_simulation(), "\n")

    # VoIP Introduction
    print("VoIP (Voice over Internet Protocol):")
    print(voip_introduction(), "\n")

# Run all protocol simulations
if __name__ == "__main__":
    run_all_protocols()
