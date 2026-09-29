from .extensions import db

class Expense(db.Model):
    __tablename__ = "expenses"

    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(100), nullable=False)
    item = db.Column(db.String(100), nullable=False)
    expense_date = db.Column(db.Date, nullable=False)
    amount = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return (
            f"<Expense {self.id}: "
            f"{self.category} - {self.item}>"
        )