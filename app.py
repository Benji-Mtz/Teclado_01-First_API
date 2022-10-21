from flask import Flask, request

app = Flask('__name__')

stores = [
    {
        "name": "My Store",
        "items": [
            {
                "name": "Chair",
                "price": 15.99
            }
        ]
    }
]

@app.get("/store") #http://127.0.0.1:5000/store
def get_stores():
    return {"stores": stores}

@app.post("/store")
def create_store():
    reques_data = request.get_json()
    new_store = {"name": reques_data["name"], "items": []}
    stores.append(new_store)
    return new_store, 201

@app.post("/store/<string:name>/item")
def create_item():
    pass