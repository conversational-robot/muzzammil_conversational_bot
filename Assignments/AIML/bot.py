import aiml

# Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.learn("eduoram.xml")

# Press CTRL-C to break this loop
while True:
	msg = input("ME: ")
	if msg == "exit":
		break
	else:	
		print("BOT:"+kernel.respond(msg))
