from asyncio.windows_events import NULL
import os
import sys

import grpc
from twitter_pb2 import Tweet, GetTimelineRequest, PostTweetRequest, FollowUserRequest
from twitter_pb2_grpc import TwitterServiceStub

def printGreeting(user_name):
    print('Hello', user_name, 'you are now succesfully connected to server!\n')

def printInfo():
    print('You are now logged as', user_name, '\n')
    print('You can pick a number to do one of following commands:')
    print('1. Post a new tweet')
    print('2. Look for last added tweets (if they were added before)')
    print('3. Quit')
    decision = input('Picked number: ')
    os.system('cls')
    return decision

def run_client():
    channel = grpc.insecure_channel('localhost:50051')
    stub = TwitterServiceStub(channel)

    # Follow another user
    request = FollowUserRequest(user=user_name, user_to_follow='user2')
    response = stub.FollowUser(request)
    if response.success == True:
        printGreeting(user_name)
        while(1):
            decision = printInfo()
            if decision.isnumeric() == False:
                continue
            if int(decision) == 3:
                sys.exit()
            elif int(decision) == 2:
                print('How many tweets you want to display ?')
                tweetsToDisplay = input('Picked number: ')
                while(tweetsToDisplay.isnumeric() == False or int(tweetsToDisplay) < 1):
                    print('Enter integer number that is greater than 0, try again!')
                    tweetsToDisplay = input('How many tweets you want to display ?\n')
                # Get the timeline for a user
                request = GetTimelineRequest(user=user_name, count=int(tweetsToDisplay))
                response = stub.GetTimeline(request)
                print('These are last', tweetsToDisplay, 'tweets:\n')
                print(response)
                input("Press Enter to continue...")
                os.system('cls')
            elif int(decision) == 1:
                print('Enter text for tweet:')
                tweetText = input()
                 # Post a tweet on behalf of a user
                request = PostTweetRequest(tweet=Tweet(user=user_name, text=tweetText))
                response = stub.PostTweet(request)
                if response.success == True:
                    print('Tweet was posted succesfully!')
                else:
                    print('Something went wrong!')
                input("Press Enter to continue...")
                os.system('cls')
if __name__ == '__main__':
    user_name = input('Enter name for user to connect to the server: ')
    run_client()

