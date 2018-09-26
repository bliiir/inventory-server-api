# Inventory management webserver
*Release: 0.1*


> The inventory project provides a simple API to read and write to an inventory using HTTP requests


## Files

Deploy the inventory files below to your server:

| **Filename** | **Description** |
| :-- | :-- |
| **docs_Inventory.md** | This file |
| **environment.py** | The executable wisgi server |
| **inventory.py** | The logic for the server |
| **inventory_api.txt** | The inventory itself as a json object |


## HTTP request and query method overview

| Method | Path | Query | Description | Examlpes |
| :-- | :-- | :-- | :-- | :-- |
| `GET` | `~/inventory/..` | na |Retrieve inventory at the current path depth | `~/inventory` gets the entire inventory, `~/inventory/pants` gets the number of pants in inventory |
| `POST` | `~/inventory/item` | `?number` | Add `int` `item`s to the inventory | `~/inventory/shorts?5` adds five shorts to the inventory |
| `PATCH` | Same as `POST` | Same as `POST` | Same as `POST` | `~/inventory/shorts?3` changes the shorts entry from above to 3 |
| `DELETE` | `~/inventory/item` | na | Deletes the `item` from the inventory | `~/inventory/shorts` deletes the shorts entry |



# Available API endpoints



## Get all inventory

| | |
| :-- | :-- |
| **Method** | `GET` |
| **Endpoint** | `/inventory/` |
| **Path** | - |
| **Query parameters** | - |
| **Description** | Get total inventory as json object |
| **Example** | `localhost:8000/inventory/` |

#### Sample response
```
{
    "underwear": 10,
    "socks": 4,
    "hats": "4",
    "shoes": 16,
    "pants": 3,
    "earrings": "99",
    "knickers": 66
}
```



## Get item inventory

| | |
| :-- | :-- |
| **Method** | `GET` |
| **Endpoint** | `/inventory/` |
| **Path** | `/inventory/item` |
| **Query parameters** | - |
| **Description** | Get inventory for a specific item |
| **Example** | `localhost:8000/inventory/socks` |

#### Sample response

```
socks: 4
```



## Add new item category to inventory

TODO: This method should be updated to prevent replacing existing items in the inventory

| | |
| :-- | :-- |
| **Method** | `POST` |
| **Endpoint** | `/inventory/` |
| **Path** | `/inventory/item` |
| **Query parameters** | `?number` |
| **Description** | Add `number` of `item` to inventory |
| **Example** | `localhost:8000/inventory/knickers?69` |


#### Sample response

```
file updated:
{
    "underwear": 10,
    "socks": 4,
    "hats": "4",
    "shoes": 16,
    "pants": 3,
    "earrings": "99",
    "knickers": 69
}
```





## Add to or subtract from existing inventory

TODO: This method should be updated to increment/decrement the number rather than replace the number

| | |
| :-- | :-- |
| **Method** | `PATCH` |
| **Endpoint** | `/inventory/` |
| **Path** | `/inventory/item` |
| **Query parameters** | `?number` |
| **Description** | Add `number` of `item` to inventory |
| **Example** | `localhost:8000/inventory/knickers?69` |


#### Sample response

```
file updated:
{
    "underwear": 10,
    "socks": 4,
    "hats": "4",
    "shoes": 16,
    "pants": 3,
    "earrings": "99",
    "knickers": 69
}
```

## Delete inventory

| | |
| :-- | :-- |
| **Method** | `DELETE` |
| **Endpoint** | `/inventory/` |
| **Path** | `/inventory/item` |
| **Query parameters** | - |
| **Description** | Remove `item` category from inventory |
| **Example** | `localhost:8000/inventory/knickers` |


#### Sample response


```
file updated:
{
    "underwear": 10,
    "socks": 4,
    "hats": "4",
    "shoes": 16,
    "pants": 3,
    "earrings": "99"
}
```



## Features

#### This release
- [x] Get total inventory
- [x] Get the number of a specific item from inventory
- [x] Updata an item
- [x] Add an item
- [x] Delete an item
- [x] Organise the code better
- [x] Write api docs

#### Next release

- [ ] Sort by amount/


### Contribute

- Issue Tracker: https://github.com/bliiir/ras_python_core/issues
- Source Code: https://github.com/bliiir/ras_python_core


### Support


If you are having issues, please let me know. My email address is: r@bit.io


### License

The project is licensed under the BSD license.
