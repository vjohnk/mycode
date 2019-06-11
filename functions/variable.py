#!/usr/bin/python3

def print_users(user,*users):
    print("First user argument: " , user)
    for user in users:
        print('user recieved from variable length' , user)
print('edureka','admin','cto','ceo')
