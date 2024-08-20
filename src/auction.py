class Auction:
    def __init__(self, item_name, starting_price):
        self.item_name = item_name
        self.current_bid = starting_price
        self.highest_bidder = None

    def place_bid(self, user, bid_amount):
        if bid_amount > self.current_bid:
            self.current_bid = bid_amount
            self.highest_bidder = user
            return f"Bid placed successfully! Current highest bid is {self.current_bid} by {self.highest_bidder.name}."
        else:
            return f"Bid too low! Current highest bid is {self.current_bid}."

    def get_auction_status(self):
        if self.highest_bidder:
            return f"Item: {self.item_name}, Current Highest Bid: {self.current_bid} by {self.highest_bidder.name}"
        else:
            return f"Item: {self.item_name}, No bids yet. Starting price: {self.current_bid}"
