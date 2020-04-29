# Cart Management Service

## usage

All responses will have the form

```json
{
    "data": "Mixed type holding the content of response",
    "message": "Description of what happened"
}
```
Subsequent response definitions will only detail the expected value of the `data field`

### List all products in cart

**Definition**

`GET /products`

**Response**

- `200 OK` on success

```json
[
    {
    "p_id": '123',
    "p_type": "Laptop",
    "name": "ASUS",
    "quantity": '1'
    },
    {
    "p_id": '115',
    "p_type": "Phone",
    "name": "iPhone",
    "quantity": '2'
    }   
]
```
### Adding a new product in cart

***Definition**

`POST /products`

**Arguments**

- `"p_id":string` a globally unique id for the product
- `"p_type":string` type of the product
- `"name":string` name of the product
- `"quantity":string` quantity of the product

**Response**

- `201 Created` on success

```json
{
    "p_id": '115',
    "p_type": "Phone",
    "name": "iPhone",
    "quantity": '2'
} 
```

## Lookup product in the cart

`GET /product/<p_id>`

**Response**

- `404 Not Found` if the product does not exist
- `200 OK` on success

```json
{
    "p_id": '115',
    "p_type": "Phone",
    "name": "iPhone",
    "quantity": '2'
} 
```
## Adding Existing product to cart

`PUT /product/<p_id>`

**Arguments**

- `"p_id":string` a globally unique id for the product
- `"p_type":string` type of the product
- `"name":string` name of the product
- `"quantity":string` quantity of the product

**Response**

- `201 Created` on success
- `404 Not Found` if the product does not exist

```json
{
    "p_id": '115',
    "p_type": "Phone",
    "name": "iPhone",
    "quantity": '3'
} 
```

## Delete a product from cart

**Definition**

`DELETE /product/<p_id>`

**Response**

- `404 Not Found` if the product does not exist
- `204 No Content` on success
