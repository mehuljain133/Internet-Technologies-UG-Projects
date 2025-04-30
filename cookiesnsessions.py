# Introduction to cookies and sessions, Introduction to e-commerce websites and e-carts.

import time
import random

# Introduction to Cookies
def cookies_introduction():
    explanation = """
    **Cookies** are small pieces of data stored by a web browser on the user's device. They are used to remember
    user preferences, login sessions, and tracking information. Cookies are sent between the client and the server
    with each HTTP request, allowing websites to maintain state (since HTTP is stateless).
    
    **Common Uses of Cookies**:
    1. Storing login information (authentication cookies).
    2. Remembering user preferences (theme color, language).
    3. Tracking user activity for analytics or marketing purposes.
    
    Cookies have an expiration time, after which they are automatically deleted.
    """
    return explanation

# Introduction to Sessions
def sessions_introduction():
    explanation = """
    **Sessions** are used by web servers to store data for a user's interaction across multiple pages of a website.
    Unlike cookies, sessions are stored on the server, and a unique session ID is stored in the user's browser as a cookie.
    Sessions provide a secure way to store sensitive information like login details or shopping cart contents.
    
    **How Sessions Work**:
    1. The user logs in or starts a session.
    2. The server generates a unique session ID and sends it to the user's browser.
    3. The browser sends the session ID with each subsequent request.
    4. The server uses the session ID to retrieve stored data (such as user login information).
    
    Sessions usually expire after a period of inactivity or when the user logs out.
    """
    return explanation

# Simulating Cookie Behavior
def simulate_cookies():
    print("\nSimulating Cookie Behavior...\n")
    
    # User information stored in cookies
    cookies = {
        "username": "john_doe",
        "theme": "dark",
        "preferences": {"font_size": "large", "notifications": "on"},
        "last_login": "2025-04-30"
    }
    
    # Simulate sending cookies with a request
    print("Sending cookies with HTTP request:\n", cookies)
    time.sleep(1)  # Simulate network delay
    print("Cookies received and processed by the server.\n")
    
    return cookies

# Simulating Session Behavior
def simulate_sessions():
    print("\nSimulating Session Behavior...\n")
    
    # User session data (stored on the server)
    session_data = {
        "session_id": "abc123xyz",
        "user": "john_doe",
        "cart_items": ["item_1", "item_2", "item_3"],
        "login_status": True
    }
    
    # Simulate storing session on the server
    print(f"Storing session data: {session_data}")
    time.sleep(1)  # Simulate network delay
    print("Session data stored successfully.\n")
    
    return session_data

# Introduction to E-commerce Websites
def ecommerce_website_intro():
    explanation = """
    **E-commerce websites** are platforms that facilitate buying and selling products or services over the internet.
    They allow businesses to set up online stores where customers can browse products, make purchases, and track orders.

    **Key Features of E-commerce Websites**:
    1. Product Catalog: A list of products with descriptions, images, and prices.
    2. Shopping Cart: Allows users to add, remove, and modify items before proceeding to checkout.
    3. Payment Gateway: A secure method for processing payments (e.g., credit cards, PayPal).
    4. Order Management: Tracks customer orders and handles processing, shipping, and delivery.
    5. User Account Management: Allows users to create accounts, manage their profile, and view order history.
    """
    return explanation

# Introduction to E-commerce Carts
def ecommerce_cart_intro():
    explanation = """
    **E-commerce Shopping Cart** is a virtual cart that allows users to collect items they wish to purchase before proceeding to checkout.
    It holds the list of items, their quantities, prices, and calculates the total cost, taxes, and shipping fees.

    **Key Features of E-commerce Carts**:
    1. **Add to Cart**: Users can select items from the product catalog and add them to their cart.
    2. **View Cart**: Users can view the items in the cart, adjust quantities, or remove items.
    3. **Checkout**: Users can enter shipping information, choose payment methods, and complete their purchase.
    4. **Discounts and Coupons**: The cart can apply promotional discounts or coupon codes to reduce the total price.
    5. **Cart Persistence**: The cart can persist between sessions (through cookies or sessions), allowing users to come back later.
    """
    return explanation

# Simulating an E-commerce Cart
def simulate_ecommerce_cart():
    print("\nSimulating E-commerce Cart...\n")
    
    # Mock product catalog
    product_catalog = {
        "item_1": {"name": "Laptop", "price": 1000},
        "item_2": {"name": "Smartphone", "price": 500},
        "item_3": {"name": "Headphones", "price": 150},
        "item_4": {"name": "Keyboard", "price": 100}
    }
    
    # Simulate adding products to the cart
    cart = {}
    items_to_add = random.sample(list(product_catalog.items()), 2)  # Randomly select 2 items
    
    for item_id, item in items_to_add:
        cart[item_id] = item
        print(f"Added {item['name']} to cart. Price: ${item['price']}")
    
    # Simulate checkout process
    print("\nProceeding to checkout...")
    total_price = sum(item['price'] for item in cart.values())
    print(f"Total cart value: ${total_price}")
    
    # Simulate applying a discount
    discount = 0.1  # 10% discount
    discounted_price = total_price * (1 - discount)
    print(f"Discount applied: 10% off. New total: ${discounted_price}")
    
    # Simulate payment
    payment_status = random.choice(["Success", "Failure"])
    print(f"Payment status: {payment_status}")
    
    return cart, discounted_price, payment_status

# Running the entire simulation
def run_full_simulation():
    print("Welcome to the Simulation of Cookies, Sessions, and E-commerce Websites!\n")
    
    # Simulate Cookies
    print(cookies_introduction())
    cookies_data = simulate_cookies()
    
    # Simulate Sessions
    print(sessions_introduction())
    session_data = simulate_sessions()
    
    # E-commerce Website and Cart Simulation
    print(ecommerce_website_intro())
    print(ecommerce_cart_intro())
    cart, discounted_price, payment_status = simulate_ecommerce_cart()
    
    print("\nSimulation Complete!\n")
    print(f"Final Cart Items: {cart}")
    print(f"Total Price After Discount: ${discounted_price}")
    print(f"Payment Status: {payment_status}\n")

if __name__ == "__main__":
    run_full_simulation()
