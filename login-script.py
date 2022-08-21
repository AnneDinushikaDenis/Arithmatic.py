server_username ="sasha"
server_password ="1234"

user_entered_name=input("enter your username:") 
user_entered_password=input("enter your password:")

if (server_username==user_entered_name and server_password== user_entered_password):

	 print("logged in success")

else:
	print("your password or username incorrect")
