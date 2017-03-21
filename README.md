## Setting up development

**Create virtualenv**

    virtualenv --python=python3 moberries
    ./moberries/bin/activate
    
**Install dependencies**

    pip install -r requirements.txt
    

**Apply database migrations**

    python manage.py migrate
    
**Load Initial Pizza Fixtures** :yum::yum:

    python manage.py loaddata pizza.json

## Run development servers

**Note:** Virtualenv must be activated for the following commands to work

Run django server: `python manage.py runserver`

## Running tests
    python manage.py test -v2 
    
    
## Api Guide
**Using the httpie `http` command**

- Get a List of all orders
``` bash
$ http GET localhost:8000/api/orders/
```

- Creates New Order using the order data and a new Customer if None matheche the name and address exists. 
- `pizza_id` only accepts integers from 1-7
``` bash
$ http POST localhost:8000/api/orders/ pizza_id={integer} pizza_size={35 or 50} customer_name="{char}" customer_address="{char}"
```

- Get order details 
``` bash
$ http GET localhost:8000/api/orders/{order_id}/
```

- Fully Update Order.
- Will create a new User if user data is modified
``` bash
$ http PUT localhost:8000/api/orders/{order_id}/ pizza_id={integer} pizza_size={35 or 50} customer_name="{char}" customer_address="{char}"
```

- Partialy Update Order.
- Will create a new User if user data is modified
``` bash
$ http PATCH localhost:8000/api/orders/{order_id}/ pizza_id={integer} pizza_size={35 or 50} 
```

- Delete an order entery
```bash
$ http DELETE localhost:8000/api/orders/{order_id}/
```

- Return Customer Details including a list of order history
- This full URI can be found in any order Detail named `customer`
``` bash
$ http GET localhost:8000/api/customers/{customer_id}/
```
    
    
