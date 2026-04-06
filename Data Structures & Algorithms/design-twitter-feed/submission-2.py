class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.followers = defaultdict(set)
        self.tweetIdx = 0
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.tweetIdx, tweetId])
        if len(self.tweets[userId]) > 10:
            self.tweets[userId].pop(0)

        self.tweetIdx -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        self.followers[userId].add(userId)
        for x in self.followers[userId]:
            if x in self.tweets:
                index = len(self.tweets[x]) - 1
                count, tweetId = self.tweets[x][index]
                heapq.heappush(minHeap, [count, tweetId, x, index - 1])

        while len(res) < 10 and minHeap:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                c, t = self.tweets[followeeId][index]
                heapq.heappush(minHeap, [c, t, followeeId, index - 1])

        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers:
            if followeeId in self.followers[followerId]:
                self.followers[followerId].remove(followeeId)
        
