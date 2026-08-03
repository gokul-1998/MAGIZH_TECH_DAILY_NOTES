1) What is Flask?
    - Flask is a Micro Framework
    - FastAPI modern Framework for building APIs with Python 3.6+ based on standard Python type hints.
    - Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.
1.1) What is a Framework?
    - the basic structure of something that gives it shape and strength.
    - it has certain rules , if you follow the rules you can develope easily and there are many things already build for you. you just need to use the tools.

- http server ( url )
    - 

2) what is FastAPI?
3) How is Fastapi and flask different?
4) 4 diff http methods
    - GET
    - POST
    - PUT
    - DELETE

5) why flask is micro framework?
    - Flask is considered a micro framework because it provides only the essential features needed to build a web application. It doesn't include many of the additional tools and libraries that are available in larger frameworks like Django. This makes it more lightweight and easier to learn for beginners.

6) difference between fastapi and flask
    - FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints. It is built on top of Starlette for the web parts and Pydantic for the data parts.
    - Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries. It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions.

7) name few http status codes
    - 200 OK -> Get, PUT
    - 204 No Content -> Delete
    - 201 Created -> Post
    - 400 Bad Request -> error from client
    - 401 Unauthorized
    - 403 Forbidden
    - 404 Not Found
    - 500 Internal Server Error -> error from server

8) What is json?


9) what is stateful and stateless?
    - Stateful: A stateful application is one that maintains state information across multiple requests from the same client. This means that the server keeps track of the client's previous interactions and can use that information to provide a more personalized experience. For example, a shopping cart application that remembers the items a user has added to their cart is stateful.
    - Stateless: A stateless application, on the other hand, does not maintain any state information between requests. Each request is treated as an independent transaction, and the server does not remember any previous interactions with the client. This makes stateless applications easier to scale and more resilient to failures, but it can also make them less user-friendly in some cases.
    - JWT (JSON Web Token) is a compact, URL-safe means of representing claims to be transferred between two parties. It is often used for authentication and authorization in web applications. JWTs are stateless because they contain all the necessary information about the user and their permissions, allowing the server to validate the token without needing to maintain any session state.

- if 1 user ocuupies 1 megabyte of memery, how much memeorey needed for 100 million users?
    - 100 million users * 1Megabyte = 100 million mega bytes = 100_000_000 MB

- frontend ( laptopn and mobiles ( browser))
- and backend ( server , database, api, etc)