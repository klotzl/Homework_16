import json
import json_data
from classes import *
from flask import request
from config import *


# Есть пользователь, он может быть как заказчиком, так и исполнителем.
# Пользователь с ролью Заказчик может создать Заказ.
# Пользователь с ролью Исполнитель может откликнуться на Заказ и предложить выполнить его (Offer).


@app.route("/users", methods=["GET", "POST"])
def all_users():
    if request.method == "GET":
        result = []
        for user in User.query.all():
            result.append(user.to_dict())

        return json.dumps(result), 200, {'Content-Type': 'application/json; charset=uft-8'}

    if request.method == "POST":
        user_data = json.loads(request.data)

        db.session.add(
            User(
                id=user_data.get("id"),
                first_name=user_data.get("first_name"),
                last_name=user_data.get("last_name"),
                age=user_data.get("age"),
                email=user_data.get("email"),
                role=user_data.get("role"),
                phone=user_data.get("phone"),
            )
        )
        db.session.commit()

        return "", 201


@app.route("/users/<int:uid>", methods=["GET", "PUT", "DELETE"])
def one_user(uid: int):
    if request.method == "GET":
        return json.dumps(User.query.get(uid).to_dict())
    if request.method == "PUT":
        user_data = json.loads(request.data)
        user = User.query.get(uid)

        user.first_name = user_data["first_name"]
        user.last_name = user_data["last_name"]
        user.age = user_data["age"]
        user.email = user_data["email"]
        user.role = user_data["role"]
        user.phone = user_data["phone"]

        db.session.add(user)
        db.session.commit()

        return "", 201

    if request.method == "DELETE":
        user = User.query.get(uid)

        db.session.delete(user)
        db.session.commit()

        return "", 204


@app.route("/orders", methods=["GET", "POST"])
def orders():
    if request.method == "GET":
        result = []
        for user in Order.query.all():
            result.append(user.to_dict())

        return json.dumps(result), 200, {'Content-Type': 'application/json; charset=uft-8'}

    if request.method == "POST":
        order_data = json.loads(request.data)

        db.session.add(
            Order(
                id=order_data.get("id"),
                name=order_data.get("name"),
                description=order_data.get("description"),
                start_date=order_data.get("start_date"),
                end_date=order_data.get("end_date"),
                address=order_data.get("address"),
                price=order_data.get("price"),
                customer_id=order_data.get("customer_id"),
                executor_id=order_data.get("executor_id")
            )
        )
        db.session.commit()

        return "", 201


@app.route("/orders/<int:uid>", methods=["GET", "PUT", "DELETE"])
def order(uid: int):
    if request.method == "GET":
        return json.dumps(Order.query.get(uid).to_dict()), 200, {'Content-Type': 'application/json; charset=uft-8'}

    if request.method == "PUT":
        order_data = json.loads(request.data)
        user = Order.query.get(uid)

        user.name = order_data["name"]
        user.description = order_data["description"]
        user.start_date = order_data["start_date"]
        user.end_date = order_data["end_date"]
        user.address = order_data["address"]
        user.price = order_data["price"]
        user.customer_id = order_data["customer_id"]
        user.executor_id = order_data["executor_id"]

        db.session.add(user)
        db.session.commit()

        return "", 201

    if request.method == "DELETE":
        user = Order.query.get(uid)

        db.session.delete(user)
        db.session.commit()

        return "", 204


@app.route("/offers", methods=["GET", "POST"])
def offers():
    if request.method == "GET":
        result = []
        for user in Offer.query.all():
            result.append(user.to_dict())

        return json.dumps(result), 200, {'Content-Type': 'application/json; charset=uft-8'}

    if request.method == "POST":
        offer_data = json.loads(request.data)

        db.session.add(
            Offer(
                id=offer_data.get("id"),
                order_id=offer_data.get("order_id"),
                executor_id=offer_data.get("executor_id")
            )
        )
        db.session.commit()

        return "", 201


@app.route("/offers/<int:uid>", methods=["GET", "PUT", "DELETE"])
def offer(uid: int):
    if request.method == "GET":
        return json.dumps(Offer.query.get(uid).to_dict()), 200, {'Content-Type': 'application/json; charset=uft-8'}

    if request.method == "PUT":
        offer_data = json.loads(request.data)
        user = Offer.query.get(uid)

        user.order_id = offer_data["order_id"]
        user.executor_id = offer_data["executor_id"]

        db.session.add(user)
        db.session.commit()

        return "", 201

    if request.method == "DELETE":
        user = Offer.query.get(uid)

        db.session.delete(user)
        db.session.commit()

        return "", 204


def init_database():
    db.drop_all()
    db.create_all()

    for user_data in json_data.users:
        db.session.add(
            User(
                id=user_data.get("id"),
                first_name=user_data.get("first_name"),
                last_name=user_data.get("last_name"),
                age=user_data.get("age"),
                email=user_data.get("email"),
                role=user_data.get("role"),
                phone=user_data.get("phone"),
            )
        )
        db.session.commit()

    for order_data in json_data.orders:
        db.session.add(
            Order(
                id=order_data.get("id"),
                name=order_data.get("name"),
                description=order_data.get("description"),
                start_date=order_data.get("start_date"),
                end_date=order_data.get("end_date"),
                address=order_data.get("address"),
                price=order_data.get("price"),
                customer_id=order_data.get("customer_id"),
                executor_id=order_data.get("executor_id")
            )
        )
        db.session.commit()

    for offer_data in json_data.offers:
        db.session.add(
            Offer(
                id=offer_data.get("id"),
                order_id=offer_data.get("order_id"),
                executor_id=offer_data.get("executor_id"),
            )
        )
        db.session.commit()


if __name__ == '__main__':
    with app.app_context():
        init_database()
        app.run(debug=True)
