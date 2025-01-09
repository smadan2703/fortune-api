import random

def get_random_quote():
    """
    Returns a random quote from a predefined list of quotes.
    """
    quotes = [
        {"content": "The greatest glory in living lies not in never falling, but in rising every time we fall.", "author": "Nelson Mandela"},
        {"content": "The way to get started is to quit talking and begin doing.", "author": "Walt Disney"},
        {"content": "Your time is limited, so don't waste it living someone else's life.", "author": "Steve Jobs"},
        {"content": "If life were predictable it would cease to be life, and be without flavor.", "author": "Eleanor Roosevelt"},
        {"content": "If you look at what you have in life, you'll always have more.", "author": "Oprah Winfrey"},
    ]

    random_quote = random.choice(quotes)
    return f"\"{random_quote['content']}\" - {random_quote['author']}"

if __name__ == "__main__":
    print("Fetching a random quote...")
    quote = get_random_quote()
    print(quote)
