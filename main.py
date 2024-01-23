import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Define the callback functions
def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_text('''Hi! I am a Bot always ready to help student. How can I assist you? 
        To go main menu type menu or click on /menu''')


def details(update: Update, context: CallbackContext) -> None:
    """Send a message with all project details when the command /details is issued."""
    update.message.reply_text(''' Hi! I am a Bot created by final year student 
    from kce college of engineering, Jalgaon 
    1 -> Vivek Kailas Patil
    2 -> Student names 

    project Guided By Prof.V.G.Sarode sir
    To go main menu type menu or click on /menu
    To contact us type contact or click on /help''')


def menu(update: Update, context: CallbackContext) -> None:
    """Send a message to get help or complete navigate of bot when the command /details is issued."""
    update.message.reply_text(''' Thanks you for asking here is your answer -
     This are the complete navigation of your all resource ..
     To know about my creaters type details or click on /details
      1. To Download syllabus type notes or click on /notes
      2. To Download syllabus type form or click on /ac_form
      3. To Download syllabus type books or click on /books
      4. To Download syllabus type syllabus or click on /syllabus
      5. To Download syllabus type referece lecture or click on /ref_lect
      6. To Download syllabus type report or click on /r_sample
      7. To get sample report type seminar or click on /r_sample
      8. To get result link type result or click on rs_link
      9. To get all portal links type portal or click on portal_link
      10. To get all electrical books type electrical books or click on /electrical_books
      11. To get all entc books type Entc books or click on /Entc_books
      12. To get all computer books type computer books or click on /computer_books ''')
      

#main context
def help(update: Update, context: CallbackContext) -> None:
    """Send a message to get help or complete navigate of bot when the command /details is issued."""
    update.message.reply_text(''' Thank you for asking if you have some question
     please send mail to our email id - demo@gmail.com
        To go main menu type menu or click on /menu
        To contact us type contact or click on /help ''')
    

    
def syllabus(update: Update, context: CallbackContext) -> None:
    """Send a message to get syllabus when the command /details is issued."""
    update.message.reply_text(''' Thanks you for asking here is your answer -
     please give branch name that syllabus your looking for 
     1. Type electrical syllabus or click on /electrical_syllabus
     2. Type entc syllabus or click on /Entc_syllabus
     3. Type computer syllabus or click on /computer_syllabus
        To go main menu type menu or click on /menu
      .. ''')
    


def notes(update: Update, context: CallbackContext) -> None:
    """Send a message to get all sem books and notes when the command /notes is issued."""
    update.message.reply_text(''' Thanks you for asking here is your answer -
     please give branch name that notes your looking for 
     1. Type electrical notes or click on /electrical_notes
     2. Type entc notes or click on /Entc_notes
     3. Type computer notes or click on /computer_notes
        To go main menu type menu or click on /menu
      .. ''')
    


def ac_form(update: Update, context: CallbackContext) -> None:
    """Send a message with all project details when the command /details is issued."""
    update.message.reply_text(''' Thanks you for asking here is your answer -
     I have following acadamic form links and details
     1. Scholarship form link -
     link - 
     2. Exam form link -
     link -
     3. GATE exam form link -
     link -
     4. CDAC exam details - 
        To go main menu type menu or click on /menu''')
    


def books(update: Update, context: CallbackContext) -> None:
    """Send a message to get all sem books and notes when the command /books is issued."""
    update.message.reply_text(''' Thanks you for asking here is your answer -
     please give branch name that notes your looking for 
     1. Type electrical books or click on /electrical_books
     2. Type entc books or click on /Entc_books
     3. Type computer books or click on /computer_books
        To go main menu type menu or click on /menu
      .. ''')
    

def ref_lect(update: Update, context: CallbackContext) -> None:
    """Send a message to get referece lecture when the command /details is issued."""
    update.message.reply_text(''' Referece lecture resource are work in progress
     sorry for your inconvenience 
     To go main menu type menu or click on /menu''')
    


def r_sample(update: Update, context: CallbackContext) -> None:
    """Send a message to get sample pdfs of seminar and report when the command /details is issued."""
    update.message.reply_text(''' Thanks you for asking here is your answer -
     here is your all samples pdf and word files 
     To go main menu type menu or click on /menu''')
    


def rs_link(update: Update, context: CallbackContext) -> None:
    """Send a message to get result link when the command /details is issued."""
    update.message.reply_text('''  Thanks you for asking here is your answer -
     here your result link -  
        To go main menu type menu or click on /menu''')
    
    
def portal_link(update: Update, context: CallbackContext) -> None:
    """Send a message to get portal links when the command /portal_link is issued."""
    update.message.reply_text('''Thanks you for asking here is your answer -
     here your all portal link
     1. DBATU University portal
      link - 
     2. Scholarship Portal
      link - 
     3. NPTEL Portal
      link - 
     4. Job portal
      link - 
     5. Superset
      link -  
        To go main menu type menu or click on /menu''')
    


def project_thesis(update: Update, context: CallbackContext) -> None:
    """Send a message to get portal links when the command /portal_link is issued."""
    update.message.reply_text('''Thanks you for asking here is your answer -
     here is our project thesis and presentation file link
     link- 
        To go main menu type menu or click on /menu''')



#secondary context for syllabus

def electrical_syllabus(update: Update, context: CallbackContext) -> None:
    """Send a message to get syllabus links when the command /electrical_syllabus is issued."""
    update.message.reply_text(''' Thanks you for asking here is your answer -
     please click on your specific semester link - 
     semester 1
     link - 
     semester 2
     link - 
     semester 3
     link - 
     semester 4
     link - 
     semester 5
     link - 
     semester 6
     link - 
     semester 7
     link - 
     semester 8
     link - 
        
        To go main menu type menu or click on /menu''')
    


def Entc_syllabus(update: Update, context: CallbackContext) -> None:
    """Send a message to get syllabus links when the command /electrical_syllabus is issued."""
    update.message.reply_text(''' Thanks you for asking here is your answer -
     please click on your specific semester link - 
     semester 1
     link - 
     semester 2
     link - 
     semester 3
     link - 
     semester 4
     link - 
     semester 5
     link - 
     semester 6
     link - 
     semester 7
     link - 
     semester 8
     link -  
        To go main menu type menu or click on /menu''')
    


def computer_syllabus(update: Update, context: CallbackContext) -> None:
    """Send a message to get syllabus links when the command /electrical_syllabus is issued."""
    update.message.reply_text(''' Thanks you for asking here is your answer -
     please click on your specific semester link - 
     semester 1
     link - 
     semester 2
     link - 
     semester 3
     link - 
     semester 4
     link - 
     semester 5
     link - 
     semester 6
     link - 
     semester 7
     link - 
     semester 8
     link -  
        To go main menu type menu or click on /menu ''')



#secondary context for books

def electrical_books(update: Update, context: CallbackContext) -> None:
    """Send a message to get electrical_books links when the command /electrical_books is issued."""
    update.message.reply_text(''' Thanks you for asking here is your answer -
     please click on your specific semester link - 
     semester 1
     link - 
     semester 2
     link - 
     semester 3
     link - 
     semester 4
     link - 
     semester 5
     link - 
     semester 6
     link - 
     semester 7
     link - 
     semester 8
     link - 
        To go main menu type menu or click on /menu''')
    


def Entc_books(update: Update, context: CallbackContext) -> None:
    """Send a message to get Entc_books links when the command /Entc_books is issued."""
    update.message.reply_text(''' Thanks you for asking here is your answer -
     please click on your specific semester link - 
     semester 1
     link - 
     semester 2
     link - 
     semester 3
     link - 
     semester 4
     link - 
     semester 5
     link - 
     semester 6
     link - 
     semester 7
     link - 
     semester 8
     link - 
        To go main menu type menu or click on /menu''')
    


def computer_books(update: Update, context: CallbackContext) -> None:
    """Send a message to get computer_books links when the command /computer_books is issued."""
    update.message.reply_text(''' Thanks you for asking here is your answer -
     please click on your specific semester link - 
     semester 1
     link - 
     semester 2
     link - 
     semester 3
     link - 
     semester 4
     link - 
     semester 5
     link - 
     semester 6
     link - 
     semester 7
     link - 
     semester 8
     link - 
        To go main menu type menu or click on /menu''')
    


#secondary context for notes

def electrical_notes(update: Update, context: CallbackContext) -> None:
    """Send a message to get electrical_notes links when the command /electrical_notes is issued."""
    update.message.reply_text(''' Thanks you for asking here is your answer -
     please click on your specific semester link - 
     semester 1
     link - 
     semester 2
     link - 
     semester 3
     link - 
     semester 4
     link - 
     semester 5
     link - 
     semester 6
     link - 
     semester 7
     link - 
     semester 8
     link - 
        To go main menu type menu or click on /menu''')
    


def Entc_notes(update: Update, context: CallbackContext) -> None:
    """Send a message to get Entc_notes links when the command /Entc_notes is issued."""
    update.message.reply_text(''' Thanks you for asking here is your answer -
     please click on your specific semester link - 
     semester 1
     link - 
     semester 2
     link - 
     semester 3
     link - 
     semester 4
     link - 
     semester 5
     link - 
     semester 6
     link - 
     semester 7
     link - 
     semester 8
     link - 
        To go main menu type menu or click on /menu''')
    


def computer_notes(update: Update, context: CallbackContext) -> None:
    """Send a message to get computer_notes links when the command /computer_notes is issued."""
    update.message.reply_text(''' Thanks you for asking here is your answer -
     please click on your specific semester link - 
     semester 1
     link - 
     semester 2
     link - 
     semester 3
     link - 
     semester 4
     link - 
     semester 5
     link - 
     semester 6
     link - 
     semester 7
     link - 
     semester 8
     link - 
        To go main menu type menu or click on /menu''')
#secondary context for portal links



def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user's message."""
    user_message = update.message.text
    if user_message.lower() == 'hi':
        reply_message = '''      Hello! Student
        Welcome to the Student Help Chat Bot! 
        I'm here to assist you with any acadmic 
        material or concerns you may have regarding your 
        academic journey. 
        Whether you need help with a subject notes, books, syllabus, 
        or referece video lectures, 
        I'm here to support you.
        Please don't hesitate to ask me help - 
        I'm always here and ready to help!
        To get my creators info type or click on /details
        To go main menu type menu or click on /menu
        To contact us type contact or click on /help'''



    elif user_message.lower() == 'how are you':
        reply_message = '''I am doing well, thanks for asking!
        To go main menu type menu or click on /menu'''



    elif user_message.lower() == 'what is your name?':
        reply_message = 'My name is student Chatbot!'




    elif user_message.lower() == 'electrical syllabus':
        reply_message = ''' Thanks you for asking here is your answer -
     please click on your specific semester link - 
     semester 1
     link - 
     semester 2
     link - 
     semester 3
     link - 
     semester 4
     link - 
     semester 5
     link - 
     semester 6
     link - 
     semester 7
     link - 
     semester 8
     link - 
        To go main menu type menu or click on /menu'''



    elif user_message.lower() == 'entc syllabus':
        reply_message = '''Thanks you for asking here is your answer -
     please click on your specific semester link - 
     semester 1
     link - 
     semester 2
     link - 
     semester 3
     link - 
     semester 4
     link - 
     semester 5
     link - 
     semester 6
     link - 
     semester 7
     link - 
     semester 8
     link -
        To go main menu type menu or click on /menu'''



    elif user_message.lower() == 'computer syllabus':
        reply_message = '''Thanks you for asking here is your answer -
     please click on your specific semester link - 
     semester 1
     link - 
     semester 2
     link - 
     semester 3
     link - 
     semester 4
     link - 
     semester 5
     link - 
     semester 6
     link - 
     semester 7
     link - 
     semester 8
     link -
        To go main menu type menu or click on /menu'''



    elif user_message.lower() == 'electrical notes':
        reply_message = '''Thanks you for asking here is your answer -
     please click on your specific semester link - 
     semester 1
     link - 
     semester 2
     link - 
     semester 3
     link - 
     semester 4
     link - 
     semester 5
     link - 
     semester 6
     link - 
     semester 7
     link - 
     semester 8
     link -
        To go main menu type menu or click on /menu'''



    elif user_message.lower() == 'entc notes':
        reply_message = '''Thanks you for asking here is your answer -
     please click on your specific semester link - 
     semester 1
     link - 
     semester 2
     link - 
     semester 3
     link - 
     semester 4
     link - 
     semester 5
     link - 
     semester 6
     link - 
     semester 7
     link - 
     semester 8
     link -
        To go main menu type menu or click on /menu'''



    elif user_message.lower() == 'computer notes':
        reply_message = '''Thanks you for asking here is your answer -
     please click on your specific semester link - 
     semester 1
     link - 
     semester 2
     link - 
     semester 3
     link - 
     semester 4
     link - 
     semester 5
     link - 
     semester 6
     link - 
     semester 7
     link - 
     semester 8
     link -
        To go main menu type menu or click on /menu'''



    elif user_message.lower() == 'electrical books':
        reply_message = '''Thanks you for asking here is your answer -
     please click on your specific semester link - 
     semester 1
     link - 
     semester 2
     link - 
     semester 3
     link - 
     semester 4
     link - 
     semester 5
     link - 
     semester 6
     link - 
     semester 7
     link - 
     semester 8
     link -'''
        


    elif user_message.lower() == 'entc books':
        reply_message = '''Thanks you for asking here is your answer -
     please click on your specific semester link - 
     semester 1
     link - 
     semester 2
     link - 
     semester 3
     link - 
     semester 4
     link - 
     semester 5
     link - 
     semester 6
     link - 
     semester 7
     link - 
     semester 8
     link -
        To go main menu type menu or click on /menu'''


    elif user_message.lower() == 'computer books':
        reply_message = '''Thanks you for asking here is your answer -
     please click on your specific semester link - 
     semester 1
     link - 
     semester 2
     link - 
     semester 3
     link - 
     semester 4
     link - 
     semester 5
     link - 
     semester 6
     link - 
     semester 7
     link - 
     semester 8
     link -'''
        
    elif user_message.lower() == 'seminar':
        reply_message = '''Thanks you for asking here is your answer -
     here is your all samples pdf and word files - 
        To go main menu type menu or click on /menu'''


    elif user_message.lower() == 'report':
        reply_message = '''Thanks you for asking here is your answer -
     here is your all samples pdf and word files - 
        To go main menu type menu or click on /menu'''


    elif user_message.lower() == 'portal':
        reply_message = '''Thanks you for asking here is your answer -
     here your all portal link
     1. DBATU University portal
      link - 
     2. Scholarship Portal
      link - 
     3. NPTEL Portal
      link - 
     4. Job portal
      link - 
     5. Superset
      link -  
        To go main menu type menu or click on /menu'''


    elif user_message.lower() == 'result':
        reply_message = '''link - '''


    elif user_message.lower() == 'referece lecture':
        reply_message = '''Referece lecture resource are work in progress
     sorry for your inconvenience'''
        

    elif user_message.lower() == 'form':
        reply_message = '''Thanks you for asking here is your answer -
     I have following acadamic form links and details
     1. Scholarship form link -
     link - 
     2. Exam form link -
     link -
     3. GATE exam form link -
     link -
     4. CDAC exam details -
        To go main menu type menu or click on /menu'''


    elif user_message.lower() == 'menu':
        reply_message = '''Thanks you for asking here is your answer -
     This are the complete navigation of your all resource ..
     To know about my creaters type details or click on /details
      1. To Download syllabus type notes or click on /notes
      2. To Download syllabus type form or click on /ac_form
      3. To Download syllabus type books or click on /books
      4. To Download syllabus type syllabus or click on /syllabus
      5. To Download syllabus type referece lecture or click on /ref_lect
      6. To Download syllabus type report or click on /r_sample
      7. To get sample report type seminar or click on /r_sample
      8. To get result link type result or click on rs_link
      9. To get all portal links type portal or click on portal_link
      10. To get all electrical books type electrical books or click on /electrical_books
      11. To get all entc books type Entc books or click on /Entc_books
      12. To get all computer books type computer books or click on /computer_books '''
        

    elif user_message.lower() == 'syllabus':
        reply_message = '''Thanks you for asking here is your answer -
     please give branch name that syllabus your looking for 
     1. Type electrical syllabus or click on /electrical_syllabus
     2. Type entc syllabus or click on /Entc_syllabus
     3. Type computer syllabus or click on /computer_syllabus
        To go main menu type menu or click on /menu'''


    elif user_message.lower() == 'books':
        reply_message = '''Thanks you for asking here is your answer -
     please give branch name that notes your looking for 
     1. Type electrical books or click on /electrical_books
     2. Type entc books or click on /Entc_books
     3. Type computer books or click on /computer_books
        To go main menu type menu or click on /menu'''



    elif user_message.lower() == 'notes':
        reply_message = '''Thanks you for asking here is your answer -
     please give branch name that notes your looking for 
     1. Type electrical notes or click on /electrical_notes
     2. Type entc notes or click on /Entc_notes
     3. Type computer notes or click on /computer_notes
        To go main menu type menu or click on /menu'''


    elif user_message.lower() == 'contact':
        reply_message = '''hank you for asking if you have some question
     please send mail to our email id - demo@gmail.com'''
        

    elif user_message.lower() == 'project report':
        reply_message = '''here is our project report link - 
        To go main menu type menu or click on /menu'''

   
    elif user_message.lower() == 'project report':
        reply_message = '''You're welcome! It was my pleasure to assist you. 
        If you have any further questions or need any more help, 
        feel free to reach out to me again. Have a great day! 
        To go main menu type menu or click on /menu
        To contact us type contact or click on /help'
        '''


    else:
        reply_message = ''' I am sorry, I did not understand your message. 
        Could you please rephrase it? 
        To go main menu type menu or click on /menu
        To contact us type contact or click on /help '''



    update.message.reply_text(reply_message)



def main() -> None:
    """Start the bot."""
    # Set up the Updater and dispatcher
    updater = Updater("6137753548:AAFeyfWHIzu0S5CXIL8gjTSMcV0dFSfk_TQ")
    dispatcher = updater.dispatcher



    # Define the command handlers
    start_handler = CommandHandler('start', start)
    details_handler = CommandHandler('details', details)
    help_handler = CommandHandler('help',help)
    menu_handler = CommandHandler('menu',menu)
    #Define the command handlers for main menu
    syllabus_handler = CommandHandler('syllabus',syllabus)
    notes_handler = CommandHandler('notes',notes)
    ac_form_handler = CommandHandler('ac_form',ac_form)
    books_handler = CommandHandler('books',books)
    ref_lect_handler = CommandHandler('ref_lect',ref_lect)
    r_sample_handler = CommandHandler('r_sample',r_sample)
    rs_link_handler = CommandHandler('rs_link',rs_link)
    portal_link_handler = CommandHandler('portal_link',portal_link)
    #Define the command handlers for syllabus
    electrical_syllabus_handler = CommandHandler('portal_link',electrical_syllabus)
    Entc_syllabus_handler = CommandHandler('Entc_syllabus',Entc_syllabus)
    computer_syllabus_handler = CommandHandler('computer_syllabus',computer_syllabus)
    #Define the command handlers for syllabus
    electrical_books_handler = CommandHandler('electrical_books',electrical_books)
    Entc_books_handler = CommandHandler('Entc_books',Entc_books)
    computer_books_handler = CommandHandler('computer_books',computer_books)
    #Define the command handlers for syllabus
    electrical_notes_handler = CommandHandler('electrical_notes',electrical_notes)
    Entc_notes_handler = CommandHandler('Entc_notes',Entc_notes)
    computer_notes_handler = CommandHandler('computer_notes',computer_notes)
    project_thesis_handler = CommandHandler('project_thesis',project_thesis)




    # Define the message handler
    message_handler = MessageHandler(Filters.text & (~Filters.command), echo)



    # Add the handlers to the dispatcher
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(message_handler)
    dispatcher.add_handler(details_handler)
    dispatcher.add_handler(help_handler)
    dispatcher.add_handler(menu_handler)
    dispatcher.add_handler(syllabus_handler)
    dispatcher.add_handler(notes_handler)
    dispatcher.add_handler(ac_form_handler)
    dispatcher.add_handler(books_handler)
    dispatcher.add_handler(ref_lect_handler)
    dispatcher.add_handler(r_sample_handler)
    dispatcher.add_handler(rs_link_handler)
    dispatcher.add_handler(portal_link_handler)
    dispatcher.add_handler(electrical_syllabus_handler)
    dispatcher.add_handler(Entc_syllabus_handler)
    dispatcher.add_handler(computer_syllabus_handler)
    dispatcher.add_handler(electrical_books_handler)
    dispatcher.add_handler(Entc_books_handler)
    dispatcher.add_handler(computer_books_handler)
    dispatcher.add_handler(electrical_notes_handler)
    dispatcher.add_handler(Entc_notes_handler)
    dispatcher.add_handler(computer_notes_handler)

    # Start the bot
    updater.start_polling()
    logging.info("Bot started")
    updater.idle()


if __name__ == '__main__':
    main()


