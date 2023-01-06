import grpc

from twitter_pb2 import Tweet, GetTimelineRequest, PostTweetRequest, FollowUserRequest
from twitter_pb2_grpc import TwitterServiceStub

def run_client():
    channel = grpc.insecure_channel('localhost:50051')
    stub = TwitterServiceStub(channel)

    # Get the timeline for a user
    request = GetTimelineRequest(user='user1', count=10)
    response = stub.GetTimeline(request)
    print(response)

    # Post a tweet on behalf of a user
    request = PostTweetRequest(tweet=Tweet(user='user1', text='Hello, world!'))
    response = stub.PostTweet(request)
    print(response)

    # Follow another user
    request = FollowUserRequest(user='user1', user_to_follow='user2')
    response = stub.FollowUser(request)
    print(response)

if __name__ == '__main__':
    run_client()
