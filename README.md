# day-54_intro_to_Flask
Day 54 of 100.

The intro to the Flask framework. I'll be able to use this for web applications. Flask is a lightweight back-end framework that comes pre-built with code so we don't have to reinvent the wheel. Flask seems more fitting for beginners whereas Django is for larger commercial projects.

Front-End/Back-End explained (Restaurant analogy)
Client - (Where the customers sits)
Server - (Kitchen, where the chefs work)
Database - (Cabinets and storage, where ingredients and tools are kept)
After the client makes a request, the server gets the tools and ingredients from the database and prepares the meal in the kitchen before bringing the result back to the client.

Anyway, here is my first decorator and usage of Flask. What it's decorating are functions. The long and short of it is each function's runtime is being recorded and printed out on the console. Decorators are interesting, it is pretty much a function applying its effect to another function, or even a route/url
