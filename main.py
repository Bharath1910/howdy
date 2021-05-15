import os
import telebot 
import praw
import time
import random
from telebot import types
from prsaw import RandomStuff

#PRSAW
rs = RandomStuff()

#telegram API 
api_key = os.environ['Tele_API_key']

bot = telebot.TeleBot(api_key)

#PRAW API
reddit = praw.Reddit(client_id = os.environ['Reddit_client_id'],
					client_secret = os.environ['Reddit_client_secret'],
					username = os.environ['Reddit_usr'],
					password = os.environ['Reddit_pass'],
					user_agent = os.environ['Reddit_usr_agent'])

top_original_memes = reddit.subreddit("memes").top(limit = 100)
top_programming_memes = reddit.subreddit("ProgrammerHumor").top(limit = 100)


meme_post_list = []
for submission in top_original_memes:
	meme_post_list.append(submission)

programming_meme_post = []
for submission in top_programming_memes:
	programming_meme_post.append(submission)


#telebot
@bot.message_handler(commands=['help'])
def help_command(message):
   keyboard = telebot.types.InlineKeyboardMarkup()
   keyboard.row(
      	telebot.types.InlineKeyboardButton(
           'Message the developer', url='telegram.me/pythonnotfound'
		  ),
		telebot.types.InlineKeyboardButton(
			'Github', url = "https://github.com/bharath1910"	
       )
   )

   
   bot.send_message(
       message.chat.id,
       "Hello There, This is Howdy. \n \nVersion 1.2.1 /version for more information  \n For the time being, I have been programmed to do these things \n \n 1. /help - Brings up this message. \n 2. /whoami - Gives information about the user. \n 3. /start - sends memes. \n 4. /version - Version's info of the bot and bug fixes\n \n For further information, message the developer. ",
       reply_markup=keyboard
   )

@bot.message_handler(commands=['whoami'])
def whoami(message):


	markup = types.ReplyKeyboardMarkup(row_width=2)
	id_button = types.KeyboardButton('User ID')
	first_name_button = types.KeyboardButton('First Name')
	last_name_button = types.KeyboardButton('Last Name')
	username_button = types.KeyboardButton('Username')

	markup.add(
		id_button,
		first_name_button,
		last_name_button,
		username_button
	)

	bot.send_message(
		message.chat.id,
		"Which information you want?",
		reply_markup = markup
	)

	'''bot.send_message(message.chat.id,
					f"Username : {user_info['username']} \n" +
					f"First Name : {user_info['first_name']} \n" +
					f"Last Name : {user_info['last_name']} \n" +
					f"User ID : {user_info['id']} \n")'''

@bot.message_handler(commands=['none'])
def some(message):
   	#keyboard = telebot.types.InlineKeyboardMarkup()

	markup = types.ReplyKeyboardMarkup(row_width=2)
	itembtn1 = types.KeyboardButton('/help')
	itembtn2 = types.KeyboardButton('/whoami')
	markup.row(itembtn1, itembtn2)
	

	#Keyboard.add(telebot.types.InlineKeyboardButton('hi',url='https://reddit.com'))
	bot.send_message(message.chat.id, "Choose any command:", reply_markup=markup)
	# or add KeyboardButton one row at a time:
	'''markup = types.ReplyKeyboardMarkup()
	itembtna = types.KeyboardButton('a')
	itembtnv = types.KeyboardButton('v')
	itembtnc = types.KeyboardButton('c')
	itembtnd = types.KeyboardButton('d')
	itembtne = types.KeyboardButton('e')
	markup.row(itembtna, itembtnv)
	markup.row(itembtnc, itembtnd, itembtne)
	bot.send_message(message.chat.id, "Choose one letter:", reply_markup=markup)'''


@bot.message_handler(commands=['start'])
def message_memes(message):
	markup = types.ReplyKeyboardMarkup(row_width=2)
	markup.add(
		types.KeyboardButton('Memes')
	)
	bot.send_message(message.chat.id,'Hey there!',reply_markup=markup)


@bot.message_handler(func = lambda msg: msg.text is not None and '/' not in msg.text)
def Memes(message):
	#user info
	user_info = {
		'id': message.from_user.id,
		'first_name': message.from_user.first_name,
		'last_name': message.from_user.last_name,
		'username': message.from_user.username,
		}


	if message.text == "Memes":
		markup = types.ReplyKeyboardMarkup(row_width=2)
		markup.add(
		types.KeyboardButton('Original Memes'),
		types.KeyboardButton('Programming Memes'))
		bot.send_message(message.chat.id,"Which type of meme you want?",reply_markup=markup)

	elif message.text == "Original Memes":
		try:
			random_post = random.choice(meme_post_list)
		except Exception:
			keyboard = telebot.types.InlineKeyboardMarkup()
			keyboard.add(telebot.types.InlineKeyboardButton('Message the developer',url = 'telegram.me/pythonnotfound'))
			bot.send_message(message.chat.id,"Bot broke, Try again later or message the developer",reply_markup=keyboard)

		name = random_post.title
		url = random_post.url

		bot.send_photo(message.chat.id, url,caption = name)

	elif message.text == "Programming Memes":
		try:
			random_post = random.choice(programming_meme_post)
		
		except Exception:
			keyboard = telebot.types.InlineKeyboardMarkup()
			keyboard.add(telebot.types.InlineKeyboardButton('Message the developer',url = 'telegram.me/pythonnotfound'))
			bot.send_message(message.chat.id,"Bot broke, Try again later or message the developer",reply_markup=keyboard)
		
		name = random_post.title
		url = random_post.url

		bot.send_photo(message.chat.id, url,caption = name)

	elif message.text == "Username":
		try:
			bot.send_message(message.chat.id, f"Username : {user_info['username']}")
		except Exception:
			keyboard = telebot.types.InlineKeyboardMarkup()
			keyboard.add(telebot.types.InlineKeyboardButton('Message the developer',url = 'telegram.me/pythonnotfound'))
			bot.send_message(message.chat.id,"Bot broke, Try again later or message the developer",reply_markup=keyboard)

	elif message.text == "First Name":
		try:
			bot.send_message(message.chat.id, f"First Name : {user_info['first_name']}")
		
		except Exception:
			keyboard = telebot.types.InlineKeyboardMarkup()
			keyboard.add(telebot.types.InlineKeyboardButton('Message the developer',url = 'telegram.me/pythonnotfound'))
			bot.send_message(message.chat.id,"Bot broke, Try again later or message the developer",reply_markup=keyboard)			

	elif message.text == "Last Name":
		try:
			bot.send_message(message.chat.id, f"Last Name : {user_info['last_name']}")

		except Exception:
			keyboard = telebot.types.InlineKeyboardMarkup()
			keyboard.add(telebot.types.InlineKeyboardButton('Message the developer',url = 'telegram.me/pythonnotfound'))
			bot.send_message(message.chat.id,"Bot broke, Try again later or message the developer",reply_markup=keyboard)

	elif message.text == "User ID":
		try:
			bot.send_message(message.chat.id, f"User ID : {user_info['id']}") 

		except Exception:
			keyboard = telebot.types.InlineKeyboardMarkup()
			keyboard.add(telebot.types.InlineKeyboardButton('Message the developer',url = 'telegram.me/pythonnotfound'))
			bot.send_message(message.chat.id,"Bot broke, Try again later or message the developer",reply_markup=keyboard)			

	else:
		#print("user: ",message.text)
		response = rs.get_ai_response(message.text)
		bot.send_message(message.chat.id, response)
		#print("Bot: ", response)
		#bot.send_message(message.chat.id,"What are you saying?")

@bot.message_handler(commands=['version'])
def version(message):
	bot.send_photo(
		message.chat.id,
		'https://imgur.com/L5ws2MT',
		caption='Version 1.0.1 \n \nIn update 1.0.1 we got Memes! \nAnd some weird bug fixes'
	)

print("hmmm.... it kinda works.. maybe?")

while True:
	try:
		bot.polling()
	
	except Exception:
		print("Exception occured.. retrying in 10 seconds")
		time.sleep(10)
		bot.polling()
		print("Restarted")

rs.close()