#By me Ziad Abouelfarah
#fb : facebook.com/zain.abouelfarah
#gmail : ziadabouelfarah2@gmail.com

from fbchat import Client,log
from fbchat.models import *
import apiai,json,codecs, getpass


class chatbot(Client):

	def apiaiCon(self):
		self.CLIENT_ACCESS_TOKEN ="a19e56e58cd74938b112cf6ee248a12b"
		self.ai = apiai.ApiAI(self.CLIENT_ACCESS_TOKEN)
		self.request = self.ai.text_request()
		self.request.lang = "de"
		self.request.session_id = "<SESSION ID, UNIQUE FOR EACH USER>"

	def onMessage(self, author_id =None, message_object=None, thread_id=None,thread_type=ThreadType.USER, **kwargs):
		self.markAsRead(author_id)
		log.info("\033[97mMessage \033[91m{} \033[97mfrom \033[91m{} \033[97min \033[91m{}\033[97m".format(message_object,thread_id,thread_type))

		self.apiaiCon()

		msgtext = message_object.text

		self.request.query = msgtext

		response = self.request.getresponse()

		message = json.load(response)


		reply = message['result']["fulfillment"]["speech"]

		if author_id != self.uid:
			self.send(Message(text=reply), thread_id=thread_id,thread_type=thread_type)


email = str(input("your facebook email : "))
password = str(getpass.getpass("your facebook password : "))

me = chatbot(email,password)
me.listen()
		
