class Item:
    def __init__(self, name: str, price: float, image: str = ""):
        self.name = name
        self.price = price
        self.image = image


class ItemOrder:
    def __init__(self, item: Item, quantity: int = 1):
        self.item = item
        self.quantity = quantity


class Cart:
    def __init__(self):
        self._lines = []

    def get_total(self):
        total = 0
        for line in self._lines:
            total += (line.quantity * line.item.price)

        return total

    def add_item(self, item_order: ItemOrder):
        self._lines.append(item_order)


banana = Item("banana", 49.5)
yoghurt = Item("yoghurt", 32.5)

cart = Cart()
cart.add_item(ItemOrder(banana, 2))
cart.add_item(ItemOrder(yoghurt))

print(cart.get_total())
