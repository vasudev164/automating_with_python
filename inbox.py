import imaplib
import email
import pyttsx3

host = 'imap.gmail.com'
username = 'vasudev1642002@gmail.com'
password = 'nageswararao'

mail = imaplib.IMAP4_SSL(host)
mail.login(username, password)
mail.select("inbox", readonly=True)

_, search_data = mail.search(None, 'UNSEEN')

# ----------------------
textSpeech = "Yoy have ", str(len(search_data[0].split())), "mails unread."
engine = pyttsx3.init()

engine.setProperty('rate', 175)
engine.setProperty('volume', 2.0)
engine.say(textSpeech)
engine.runAndWait()
#-----------------------
print("Yoy have ", len(search_data[0].split()), "mails unread.")
for num in search_data[0].split():
    # print(num)
    _, data = mail.fetch(num, '(RFC822)')
    # print(data)
    _, b = data[0]
    email_message = email.message_from_bytes(b)
    # print(email_message)

    for header in ['subject', 'to', 'from', 'date']:
        print("{}: {}".format(header, email_message[header]))

    for part in email_message.walk():
        if part.get_content_type() == "text/plain":
            body = part.get_payload(decode=True)
            print(body.decode())
        elif part.get_content_type() == "text/html":
            html_body = part.get_payload(decode=True)
            print(html_body.decode())

# print(search_data)
mail.close()
mail.logout()
