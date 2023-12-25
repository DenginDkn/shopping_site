from flask import Flask, render_template, request

app = Flask(__name__)

products = [
    {"product_no": 1, "description": "Gray Fleece", "price": 29.99, "image": "product1.jpg", "category": "Clothing"},
    {"product_no": 2, "description": "Blue Pant", "price": 39.99, "image": "product2.jpg", "category": "Clothing"},
    {"product_no": 3, "description": "Knit Sweater", "price": 15.99, "image": "product3.jpg", "category": "Clothing"},
    {"product_no": 4, "description": "Knit Dress", "price": 17.99, "image": "product4.jpg", "category": "Clothing"},
    {"product_no": 5, "description": "Plaid Shirt", "price": 45.99, "image": "product5.jpg", "category": "Clothing"},
    {"product_no": 6, "description": "Teddy Coat", "price": 54.99, "image": "product6.jpg", "category": "Clothing"},
    {"product_no": 7, "description": "One Shoulder Blouse", "price": 25.99, "image": "product7.jpg", "category": "Clothing"},
    {"product_no": 8, "description": "Black Leather Jacket", "price": 22.99, "image": "product8.jpg", "category": "Clothing"},
    {"product_no": 9, "description": "Black Short Skirt", "price": 65.99, "image": "product9.jpg", "category": "Clothing"},
    {"product_no": 10, "description": "Pajama Set", "price": 45.99, "image": "product10.jpg", "category": "Clothing"},
]

@app.route('/')
def home():
    return render_template('home.html', products=products)

@app.route('/search', methods=['GET', 'POST'])
def search():
    query = request.args.get('q', '')
    results = [p for p in products if query.lower() in str(p).lower()]

    if request.method == 'POST':
        return redirect(url_for('search_results', query=query))

    return render_template('search_results.html', results=results, query=query)

@app.route('/search_results/<query>')
def search_results(query):
    results = [p for p in products if query.lower() in str(p).lower()]
    return render_template('search_results.html', results=results, query=query)

@app.route('/product/<int:product_no>')
def product_detail(product_no):
    product = next((p for p in products if p['product_no'] == product_no), None)
    return render_template('product_detail.html', product=product)

if __name__ == '__main__':
    app.run(debug=True)