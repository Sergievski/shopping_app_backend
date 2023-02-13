Shopping Cart project using django and react
Project includes:
Front end in React.js:
react front end that will show the following:
•	products screen
•	cart screen
should contain the following actions:
•	Show all products
•	Show products in Cart
•	Add a product to Cart
•	Remove from Cart
•	Update quantity in Cart
Back end (api) in Django
an api written in django using djangorestframework
the api will include:
Products
Product will have a name, description and image
•	get products
•	add product
•	get single product
•	delete product the delete action - should not delete but mark as archived (therefore the get products, search products should bring only product where archived=False)
•	update product
CartItem
Cart item will contain 2 fields:
1.	product as foreign key
2.	quantity
•	get CartItems
•	get single CartItem
•	add CartItem
•	Delete CartItem - also archive instead of delete
•	Update CartItem
