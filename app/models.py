class Expense:
    def __init__(self, id, category, item, date, price):
        self.id = id
        self.category = category
        self.item = item
        self.date = date
        self.price = price

    def __repr__(self):
        return (
            
            f"Expense(id={self.id!r}, "
            f"category= {self.category!r}"
            f"item={self.item!r}, "
            f"date={self.date!r}, "
            f"price={self.price!r})"
        )

    def __str__(self):
        return (
            f"id: {self.id} | "
            f"Category: {self.category} | "
            f"Item: {self.item} | "
            f"Date: {self.date} | "
            f"Price: ₦{self.price}"
        )

    def __eq__(self, other):
        if not isinstance(other, Expense):
            return NotImplemented

        return (
            self.id == other.id
            and self.category == other.category
            and self.item == other.item
            and self.date == other.date
            and self.price == other.price
        )

    def to_dict(self):
        return {
            "id": self.id,
            "category": self.category,
            "item": self.item,
            "date": self.date,
            "price": self.price,
        }