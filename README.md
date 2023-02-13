Django e-Commerce Project Readme
Introduction
This is a Django based e-commerce project, which allows users to view, add, edit and delete products. The project also allows users to add products to their shopping cart, view their shopping cart and edit/delete items from their shopping cart.

Requirements
Python 3.6 or above
Django 3.2 or above
Django REST framework
Project Structure
The project has the following structure:

product app: This app contains the main models for the project, including Product, Cart, and CartItem.
serializers.py: This file contains the serializers for the models defined in the product app.
views.py: This file contains the views for handling HTTP requests for the models defined in the product app.
How to Run the Project
Clone the repository to your local machine.
Open a terminal and navigate to the project directory.
Install the required packages by running pip install -r requirements.txt.
Run the Django development server by running python manage.py runserver.
The project should now be accessible at http://localhost:8000/.
Endpoints
The following endpoints are available in the project:

GET /products: This endpoint returns a list of all products, filtered by a search query if provided.
POST /products: This endpoint is used to add a new product to the database.
GET /products/<pk>: This endpoint returns the details of a single product, identified by its primary key (pk).
PUT /products/<pk>: This endpoint is used to update the details of a single product, identified by its primary key (pk).
DELETE /products/<pk>: This endpoint is used to delete a single product, identified by its primary key (pk).
GET /cart: This endpoint returns a list of all items in the cart.
POST /cart: This endpoint is used to add a new item to the cart.
PUT /cart/<pk>: This endpoint is used to update the details of a single item in the cart, identified by its primary key (pk).
DELETE /cart/<pk>: This endpoint is used to delete a single item from the cart, identified by its primary key (pk).
