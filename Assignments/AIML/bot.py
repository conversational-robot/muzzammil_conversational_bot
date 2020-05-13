import aiml


kernel = aiml.Kernel()
kernel.learn("eduoram.xml")
kernel.learn("bookshelf.aiml")

out = str(kernel.respond("random"))
out = out.replace(" \\n "," \n ")
print("BOT:"+out)

while True:
	msg = input("ME: ")
	if msg == "exit":
		break
	else:	
		out = str(kernel.respond(msg))
		out = out.replace(" \\n "," \n ")
		print("BOT:"+out)