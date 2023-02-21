
Shopping website

This project is a web-based e-commerce application that allows users to browse products and make purchases online. This repository contains the Django backend code for the application, which includes API endpoints for retrieving products and cart items, as well as updating and deleting cart items. The backend is designed to work with a React-based frontend, which is hosted in a separate repository.

Installation : 

Clone the repository to your local machine.
bash
Copy code
git clone https://github.com/[USERNAME]/shopping.git
Install the required packages using pip.
Copy code
pip install -r requirements.txt
Migrate the database.
Copy code
python manage.py migrate
Run the development server.
Copy code
python manage.py runserver

Usage  - Once you have installed the application, you can use the following API endpoints to interact with the backend:

Products
GET /api/products/: Get a list of all products.
GET /api/products/:id: Get details for a single product.
Cart Items
GET /api/cart-items/: Get a list of all items in the cart.
GET /api/cart-items/:id: Get details for a single item in the cart.
POST /api/cart-items/: Add a new item to the cart.
PUT /api/cart-items/:id: Update an existing item in the cart.
DELETE /api/cart-items/:id: Delete an item from the cart.
