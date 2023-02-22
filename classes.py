import config
from sqlalchemy import Integer


class User(config.db.Model):
    __tablename__ = "user"
    id = config.db.Column(Integer, primary_key=True)
    first_name = config.db.Column(config.db.String(100))
    last_name = config.db.Column(config.db.String(100))
    age = config.db.Column(config.db.Integer)
    email = config.db.Column(config.db.String(100))
    role = config.db.Column(config.db.String(100))
    phone = config.db.Column(config.db.String(100))

    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age,
            "email": self.email,
            "role": self.role,
            "phone": self.phone,
        }


class Order(config.db.Model):
    __tablename__ = "order"
    id = config.db.Column(config.db.Integer, primary_key=True)
    name = config.db.Column(config.db.String(100))
    description = config.db.Column(config.db.String(100))
    start_date = config.db.Column(config.db.String(100))
    end_date = config.db.Column(config.db.String(100))
    address = config.db.Column(config.db.String(100))
    price = config.db.Column(config.db.Integer)
    customer_id = config.db.Column(config.db.Integer, config.db.ForeignKey(f'{User.__tablename__}.id'))
    executor_id = config.db.Column(config.db.Integer, config.db.ForeignKey(f'{User.__tablename__}.id'))

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "address": self.address,
            "price": self.price,
            "customer_id": self.customer_id,
            "executor_id": self.executor_id,

        }


class Offer(config.db.Model):
    __tablename__ = "offer"
    id = config.db.Column(config.db.Integer, primary_key=True)
    order_id = config.db.Column(config.db.Integer, config.db.ForeignKey(f'{Order.__tablename__}.id'))
    executor_id = config.db.Column(config.db.Integer, config.db.ForeignKey(f'{User.__tablename__}.id'))

    def to_dict(self):
        return {
            "id": self.id,
            "order_id": self.order_id,
            "executor_id": self.executor_id
        }
