# Shopping Site

This is a simple shopping site developed using Flask.

## Data Model

- **Product**
  - `product_no`: Unique identifier for the product.
  - `description`: Brief description of the product.
  - `price`: Price of the product.
  - `image`: Filename of the product image in the `static/images` directory.
  - `category`: Category to which the product belongs.

## Assumptions

- The project assumes a basic e-commerce scenario with products and categories.
- SQLite is used as the database.

## Setup Instructions

1. Install dependencies:
    ```bash
    pip install Flask
    ```

2. Run the application:
    ```bash
    python -m flask run
    ```

3. Open your web browser and navigate to [http://localhost:5000](http://localhost:5000).

## Hosting

The application is hosted on [PythonAnywhere](https://www.pythonanywhere.com/). You can access it [here](YOUR_PYTHONANYWHERE_URL).

## Additional Notes

- This is a basic template. Feel free to customize it based on your specific requirements.
- For any issues or improvements, please open an [issue](https://github.com/yourusername/shopping-site/issues).
