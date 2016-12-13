class merchItem:
    def __init__(self, name, price, img=None):
        self.name = name
        self.price = price
        self.image = img

items = [
    {
        'name': "Gibson guitar",
        'price': 15000,
        'img': "guitar.png"
    },
    {
        'name': "CDs",
        'price': 300,
        'img': "cd.jpg"
    },
    {
        'name': "Band T-Shirts",
        'price': 200,
        'img': "shirt.jpg"
    },
    {
        'name': "Headphones",
        'price': 400,
        'img': "headphones.jpg"
    }
]

sale_items = [merchItem(item['name'], item['price'], img=item['img']) for item in items]
