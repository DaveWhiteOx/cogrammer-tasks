class Email():

    # Class variable
    has_been_read = False


    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        
    def mark_as_read(self):
        self.has_been_read = True



# Create empty list to store emails
inbox = []

# Pre-populating inbox with three objects
def populate_inbox():
    inbox.append(Email('david@emailer.com', 'Landscape Garden', 'Need to measure up the garden for landscape quote'))
    inbox.append(Email('nicholas@jacobs.com', 'Safety Inspection', 'There is an upcoming saftey inspection for Acme'))
    inbox.append(Email('lindsey@hrservices.com', 'New Employee Badge Needed', 'A new employee badge is required for the new starter'))


def list_emails():
    # Iterate through the inbox listing the index and email subject
    print("") # Spacer so list isn't shown straight after selection text
    for idx, email in enumerate(inbox):
        print(idx, email.subject_line, sep='  ')


def read_email(idx):
    print("")
    print(f"Sender: {inbox[idx].email_address}")
    print(f"Subject: {inbox[idx].subject_line}")
    print(f"Body: \n{inbox[idx].email_content}")
    inbox[idx].mark_as_read()
    print(f"\nEmail has been marked as read.")



populate_inbox()

menu = True
while True:
    user_choice = int(input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: '''))

    # Display our inbox content so user can then choose an email to view, then mark it as read.  
    if user_choice == 1:
        list_emails()
        choice = int(input("Please enter the value of the email to read: "))
        read_email(choice)
        
    elif user_choice == 2:
        print("Your unread emails:")
        for email in inbox:
            if email.has_been_read == False:
                print(email.subject_line)
            
    elif user_choice == 3:
        break

    else:
        print("Oops - incorrect input.")
