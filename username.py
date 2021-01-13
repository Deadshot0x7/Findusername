#author : Sayyed Viquar ahmed 
#from urllib.request import urlopner
import requests
import urllib


def instagram(username):
    try:
        url="http://instagram.com/"+username
        print("Username found in  Instagram")
        return("Username found ")
    except Exception  as e :
            print("Can't find the Username ")
            return("Can't find the the username ")

def pinrest(username):
    try:
        url:"http://pinrest.com/"+username
        print("Username found in Pinrest platform")
        return("Username Found")
    except Exception as e:
        print("cant find the username")



    
        







