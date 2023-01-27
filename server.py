import grpc
from concurrent import futures
from typing import List

from twitter_pb2 import Tweet,GetTimelineResponse,PostTweetResponse,FollowUserResponse
from twitter_pb2_grpc import TwitterServiceServicer, add_TwitterServiceServicer_to_server

tweets = []

class TwitterServer(TwitterServiceServicer):

    def GetTimeline(self, request, context):
        nLastTweets = tweets[::-1][:request.count]
        user_tweets = [tweet for tweet in nLastTweets]
        #Return a list of last n tweets
        return GetTimelineResponse(tweets=user_tweets)

    def PostTweet(self, request, context):
        # Store the tweet in a database or something
        tweets.append(request.tweet)
        return PostTweetResponse(success=True)

    def FollowUser(self, request, context):
        # Make the specified user follow another user
        return FollowUserResponse(success=True)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_TwitterServiceServicer_to_server(TwitterServer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
