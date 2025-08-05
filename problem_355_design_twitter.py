from typing import List
from collections import defaultdict
from heapq import heappush, heappop, heapify


class Twitter:

    def __init__(self):
        self.posts_by_user_id = defaultdict(list)
        self.followed_by_user_id = defaultdict(set)
        self.current_time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts_by_user_id[userId].append((self.current_time, tweetId))
        self.current_time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        latest_posts = []
        heapify(latest_posts)
        followees = self.followed_by_user_id[userId]
        followees.add(userId)
        for fol_id in followees:
            posts_of_fol = self.posts_by_user_id[fol_id]
            for p in posts_of_fol:
                heappush(latest_posts, p)
                if len(latest_posts) > 10:
                    heappop(latest_posts)

        return [p[1] for p in sorted(latest_posts, key=lambda x: -x[0])]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followed_by_user_id[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        current_fols = self.followed_by_user_id[followerId]
        if followeeId != followerId and followeeId in current_fols:
            current_fols.remove(followeeId)
        self.followed_by_user_id[followerId] = current_fols


if __name__ == "__main__":
    commands = ["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
    attrs = [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
    for com, attr in zip(commands, attrs):
        if com == 'Twitter':
            res = tc = Twitter()
        elif com == 'postTweet':
            res = tc.postTweet(userId=attr[0], tweetId=attr[1])
        elif com == 'getNewsFeed':
            res = tc.getNewsFeed(userId=attr[0])
        elif com == 'follow':
            res = tc.follow(followerId=attr[0], followeeId=attr[1])
        elif com == 'unfollow':
            res = tc.follow(followerId=attr[0], followeeId=attr[1])
        print(res)