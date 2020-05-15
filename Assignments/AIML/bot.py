import aiml
import os
import csv
import random

kernel = aiml.Kernel()

if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile = "bot_brain.brn")
else:
    kernel.bootstrap(learnFiles = ["eduoram.xml","bookshelf.aiml","genre.aiml"])
    kernel.saveBrain("bot_brain.brn")

out = str(kernel.respond("random"))
out = out.replace(" \\n "," \n ")
print("BOT:"+out)

order_details=[]

prev_msg = ""
while True:
	msg = input("ME: ")
	if msg == "exit":
		break
	else:	
		out = str(kernel.respond(msg))

		if out == "Please fill in your details:":
			print("BOT:"+out)
			name = input("NAME:")
			contact = input("PHONE NUMBER:")
			address = input("ADDRESS:")
			t_s = prev_msg.find("Title:")+6
			t_e = prev_msg.find("\n",t_s)
			a_s = prev_msg.find("Author:")+7
			a_e = prev_msg.find("\n",a_s)
			p_s = prev_msg.find("Price: ")+7
			p_e = prev_msg.find("\n",p_s)
			title = prev_msg[t_s:t_e] 
			author = prev_msg[a_s:a_e] 
			price = prev_msg[p_s:p_e]
			print("BOT: You have ordered "+'"'+title+'"'+" by "+'"'+author+'"'+" costing "+'"'+price+'"')
			print("BOT:"+kernel.respond("CONFIRMATION"))#write for this
			kernel.setPredicate("name",name)
			purchase_id = random.randint(100000,999999)
			order_details = [str(purchase_id),name,contact,address,title,author,price]

		elif out == "Can you please type your Purchase Id":
			p_id = str(input("Purchase Id(Of 6 digits):"))	
			while(len(p_id)!=6):
				print("BOT:Invalid purchase id,purchase id is of six digits!!")
				p_id = str(input("Purchase Id(Of 6 digits):"))
			with open('book_orders.csv', newline='') as csvfile:
				spamreader = csv.reader(csvfile, delimiter=',')
				flag = 0
				for row in spamreader:
					if len(row)!=0 and row[0]==p_id:
						flag = 1
						hasCancelled = 0
						kernel.setPredicate("name",row[1])

						with open('cancelled.csv',newline='') as cancelled:
							reader = csv.reader(cancelled,delimiter=',')
							for line in reader:
								if len(line)!=0 and line[0]==p_id:
									hasCancelled = 1
									break
						if hasCancelled == 0:
							print("BOT:"+row[1]+",your order of book"+'"'+row[4]+'"'+" has been shipped by me to your address:")
							print(row[3])
							print("You can expect its delivery within 7 days")
							print("Do you want to cancel delivery? YES|NO")
							state = input("ME:").lower()
							if state.find("yes")!=-1 or state.find("yup")!=-1 or state.find("ya")!=-1:
								print("Your order has been cancelled successfully!!")
								with open('cancelled.csv','a+',newline='') as file:
									writer = csv.writer(file)
									writer.writerow(row)
							else:
								print("BOT:OKAY!!")
						
						else:	
							print(row[1]+",you have cancelled your order!!")	
						break	
				if flag == 0:
					print("BOT:There is no order placed under this purchase id!!")		

		elif out.find("shopping")!=-1:
			print("BOT:"+out+"\nYour purchase id is "+order_details[0]+" keep it safe for tracking your order!")
			with open('book_orders.csv', 'a+', newline='') as file:
			    writer = csv.writer(file)
			    writer.writerow(order_details)	

		else:	
			out = out.replace(" \\n "," \n ")
			print("BOT:"+out)
			prev_msg = out