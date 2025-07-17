from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Фіктивні товари
products = [
    {"id": 1, "name": "Шкіряна куртка", "price": 2199, "image": "https://static.zara.net/assets/public/f8c2/85ef/6ef847e99aa4/1078bfb542d3/07012314405-p/07012314405-p.jpg"},
    {"id": 2, "name": "Джинси Slim Fit", "price": 1499, "image": "https://static.zara.net/assets/public/f5a5/edb1/15034b3c8f2f/3eb02a1c48ec/07011348250-p/07011348250-p.jpg"},
    {"id": 3, "name": "Футболка з логотипом", "price": 699, "image": "https://static.zara.net/assets/public/3f23/3f77/9dfd4ef0ae85/9db8e15ae9d1/08453303600-p/08453303600-p.jpg"},
    {"id": 4, "name": "Білі кросівки", "price": 2499, "image": "https://static.zara.net/assets/public/05ba/f64f/b0534b67860a/1f5c44761690/07852346250-p/07852346250-p.jpg"},
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/catalog")
def catalog():
    return render_template("catalog.html", products=products)

@app.route("/product/<int:product_id>")
def product(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        return render_template("product.html", product=product)
    return "Товар не знайдено", 404

@app.route("/order", methods=["GET", "POST"])
def order():
    if request.method == "POST":
        name = request.form["name"]
        phone = request.form["phone"]
        product = request.form["product"]
        # Тут могла б бути логіка для збереження замовлення
        return f"Дякуємо, {name}! Ми зв'яжемось з вами по телефону {phone} для товару: {product}."
    return render_template("order.html")

@app.route("/admin")
def admin():
    return "<h1>Адмін-панель (в розробці)</h1>"



if __name__ == "__main__":
    app.run(debug=True)


