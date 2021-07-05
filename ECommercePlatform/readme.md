E-Commerce Portal

Create a small rest service, using Flask Api for the following actions:

1) Retrieve all the business products
  - Read products.json file
  - returned it

2) Retrieve details of a specific product based on product_id
  - get product by id
  - search in products.json(if present)
  - returned it

3) Add a product to cart
  - create cart
  - get product by id
  - search in products.json(if present)
  - added to cart
  - returned the updated cart

4) Delete a product from cart
  - Search product by product ID in cart
  - if found, removed it
  - returned the updated cart

5) List products from cart
  - returned the cart

6) Proceed to Purchase
  - created total variable
  - iterate through the items of the cart
  - added the price per item to total
  - returned the total price
