from ShopScraper import Tokopedia


tokped = Tokopedia("hoodie",lowest=True).fetch() # -> list
print(tokped)