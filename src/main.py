from auction import Auction
from user import User

def main():
    print("Welcome to the Online Auction System")

    # Create a user
    user1 = User("Alice")
    user2 = User("Bob")

    # User 1 creates an auction
    auction = user1.create_auction("Vintage Painting", 100)
    print(auction.get_auction_status())

    # User 2 places a bid
    bid_result = user2.bid_on_auction(auction, 150)
    print(bid_result)

    # Another bid by User 1
    bid_result = user1.bid_on_auction(auction, 200)
    print(bid_result)

    # Check final auction status
    print(auction.get_auction_status())

if __name__ == "__main__":
    main()
