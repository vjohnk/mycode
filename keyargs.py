#!/usr/bin/python2

def print_users(user, *users):
    print('this is 1st user' , user)

    for user in users:
        print('this is rest of the users' , user)

print_users('john' , 'jack' , 'jean')
