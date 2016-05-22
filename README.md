# mealpass

Very simple python api for Mealpass:

To use, first instantiate the mealpass class. This sends a login request to Mealpass.

`m = mealpass('myuser@email.com','mypassword')`

Next, request available meals:

`response = m.search()`

Then, reserve your lunch:

- `response = m.reserve(meal_name = u'Chicken & Lamb & Rics')`
- `response = m.reserve(restaurant_name = u'Tossed)`

Finally, you can cancel your reservation:

`response = m.cancel()`