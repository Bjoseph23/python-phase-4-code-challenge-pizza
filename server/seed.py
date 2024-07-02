#!/usr/bin/env python3

from app import app
from models import db, Restaurant, Pizza, RestaurantPizza

with app.app_context():

    # This will delete any existing rows
    # so you can run the seed file multiple times without having duplicate entries in your database
    print("Deleting data...")
    Pizza.query.delete()
    Restaurant.query.delete()
    RestaurantPizza.query.delete()

    print("Creating restaurants...")
    shack = Restaurant(name="Karen's Pizza Shack", address='address1')
    bistro = Restaurant(name="Sanjay's Pizza", address='address2')
    palace = Restaurant(name="Kiki's Pizza", address='address3')
    pizzeria = Restaurant(name="Tony's Pizzeria", address='address4')
    corner_pizza = Restaurant(name="Corner Pizza", address='address5')
    mama_mia = Restaurant(name="Mama Mia's", address='address6')
    restaurants = [shack, bistro, palace, pizzeria, corner_pizza, mama_mia]

    print("Creating pizzas...")

    cheese = Pizza(name="Emma", ingredients="Dough, Tomato Sauce, Cheese")
    pepperoni = Pizza(name="Geri", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")
    california = Pizza(name="Melanie", ingredients="Dough, Sauce, Ricotta, Red peppers, Mustard")
    veggie = Pizza(name="Victoria", ingredients="Dough, Tomato Sauce, Cheese, Olives, Peppers, Onions")
    hawaiian = Pizza(name="Hawaiian", ingredients="Dough, Tomato Sauce, Cheese, Pineapple, Ham")
    margherita = Pizza(name="Margherita", ingredients="Dough, Tomato Sauce, Fresh Mozzarella, Basil")
    pizzas = [cheese, pepperoni, california, veggie, hawaiian, margherita]

    print("Creating RestaurantPizza...")

    restaurant_pizzas = [
        RestaurantPizza(restaurant=shack, pizza=cheese, price=1),
        RestaurantPizza(restaurant=bistro, pizza=pepperoni, price=4),
        RestaurantPizza(restaurant=palace, pizza=california, price=5),
        RestaurantPizza(restaurant=pizzeria, pizza=veggie, price=3),
        RestaurantPizza(restaurant=corner_pizza, pizza=hawaiian, price=6),
        RestaurantPizza(restaurant=mama_mia, pizza=margherita, price=2),
        RestaurantPizza(restaurant=shack, pizza=pepperoni, price=7),
        RestaurantPizza(restaurant=bistro, pizza=veggie, price=4),
        RestaurantPizza(restaurant=palace, pizza=hawaiian, price=8),
        RestaurantPizza(restaurant=pizzeria, pizza=cheese, price=2),
        RestaurantPizza(restaurant=corner_pizza, pizza=margherita, price=5),
        RestaurantPizza(restaurant=mama_mia, pizza=california, price=3)
    ]

    db.session.add_all(restaurants)
    db.session.add_all(pizzas)
    db.session.add_all(restaurant_pizzas)
    db.session.commit()

    print("Seeding done!")
