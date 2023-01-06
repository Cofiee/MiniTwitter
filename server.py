import grpc
from concurrent import futures

from twitter_pb2 import Tweet,GetTimelineResponse,PostTweetResponse,FollowUserResponse
from twitter_pb2_grpc import TwitterServiceServicer, add_TwitterServiceServicer_to_server

class TwitterServer(TwitterServiceServicer):
    def GetTimeline(self, request, context):
        # Return a list of tweets for the specified user
        return GetTimelineResponse(tweets=[
            Tweet(user='user1', text='tweet1'),
            Tweet(user='user1', text='tweet2'),
            Tweet(user='user1', text='tweet3'),
        ])

    def PostTweet(self, request, context):
        # Store the tweet in a database or something
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
