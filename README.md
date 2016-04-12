# mealpass

Very simple python api for Mealpass:

To use, first instantiate the mealpass class:

`m = mealpass('myuser@email.com','mypassword')`

Then, login:

`m.login()`

Finally, request available meals:

`response = m.search()`

