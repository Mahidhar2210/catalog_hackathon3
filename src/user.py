from auction import Auction
class User:
    def __init__(self, name):
        self.name = name
        self.auctions = []

    def create_auction(self, item_name, starting_price):
        new_auction = Auction(item_name, starting_price)
        self.auctions.append(new_auction)
        return new_auction

    def bid_on_auction(self, auction, bid_amount):
        return auction.place_bid(self, bid_amount)
