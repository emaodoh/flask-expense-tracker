from .extensions import db
from datetime import datetime

class Expense(db.Model):

    __tablename__ = "expenses"

    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(100), nullable=False)
    item = db.Column(db.String(100), nullable=False)
    expense_date = db.Column(db.Date, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    user = db.relationship(
    "User",
    back_populates="expenses"
    )
    def to_dict(self):
        return {
            "id":self.id,
            "category":self.category,
            "item":self.item,
            "expense_date":self.expense_date.isoformat(),
            "amount":self.amount
        }





    def __repr__(self):
        return (
            f"<Expense {self.id}: "
            f"{self.category} - {self.item}>"
        )


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    expenses = db.relationship(
    "Expense",
    back_populates="user"
)