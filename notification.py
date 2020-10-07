import config, smtplib, investpy

from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

MY_ADDRESS = 'imdb.investing@gmail.com'
PASSWORD = 'Tegustamipassword?'

def get_contacts(filename):
    """
    Return two lists names, emails containing names and email addresses
    read from a file specified by filename.
    """

    names = []
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])
    return names, emails

def read_template(filename):
    """
    Returns a Template object comprising the contents of the
    file specified by filename.
    """

    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

def send_email(x):
    names, emails = get_contacts('mycontacts.txt') # read contacts
    message_template = read_template('message.txt')

    # set up the SMTP server
    s = smtplib.SMTP(host=config.smtp_host, port=config.smtp_port)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    # For each contact, send the email:
    for name, email in zip(names, emails):
        msg = MIMEMultipart()       # create a message

    # add in the actual person name to the message template
    description = investpy.get_stock_company_profile(stock=x, country=config.country_name, language=config.language)
    url = str(description['url'])
    info = str(description['desc'])
    message = message_template.substitute(PERSON_NAME=name.title(), STOCK_ABBV=str(x), STOCK_URL=url , STOCK_INFO=info)
    # Prints out the message body for our sake
    #print(message)

    # setup the parameters of the message
    msg['From']=MY_ADDRESS
    msg['To']=email
    msg['Subject']= str("DAILY TURNING STOCK: " + x )

    # add in the message body
    msg.attach(MIMEText(message, 'plain'))

    # send the message via the server set up earlier.
    s.send_message(msg)
    del msg

    # Terminate the SMTP session and close the connection
    s.quit()
