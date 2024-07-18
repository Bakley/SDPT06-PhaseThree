from typing import Callable, Dict

# Configuration settings
config = {
    "base_discount": 0.05,
    "premium_discount": 0.20,
    "permission_levels": {
        "admin": ["apply_discount", "calculate_price", "get_discount_function"],
        "user": [ "calculate_price", "get_discount_function"]
    }
}

# Permissions decorator
def check_permissions(permission: str) -> Callable:
    """
    Decorator to check if the user has the required permission.

    Parameters:
    permission (str): The required permission.

    Returns:
    Callable: The wrapped function if permission is granted.
    """
    def decorator(func: Callable) -> Callable:
        def wrapper(user: Dict[str, str], *args, **kwargs):
            user_role = user.get("role")
            print(user_role)
            if user_role is None:
                raise ValueError("User role is not defined.")

            user_permissions = config["permission_levels"].get(user_role, [])
            print(user_permissions)
            if permission in user_permissions:
                return func(user, *args, **kwargs)
            else:
                raise PermissionError(f"User '{user['name']}' does not have permission to execute '{func.__name__}'")
        return wrapper
    return decorator

# Discount functions
@check_permissions("apply_discount")
def discount_10(user: Dict[str, str], price: float) -> float:
    """
    Apply a 10% discount to the price.

    Parameters:
    user (Dict[str, str]): The user applying the discount.
    price (float): The original price.

    Returns:
    float: The discounted price.
    """
    return price * 0.9

@check_permissions("apply_discount")
def discount_20(user: Dict[str, str], price: float) -> float:
    """
    Apply a 20% discount to the price.

    Parameters:
    user (Dict[str, str]): The user applying the discount.
    price (float): The original price.

    Returns:
    float: The discounted price.
    """
    return price * 0.8

@check_permissions("calculate_price")
def calculate_price(user: Dict[str, str], base_price: float, discount_func: Callable) -> float:
    """
    Calculate the final price after applying a discount.

    Parameters:
    user (Dict[str, str]): The user calculating the price.
    base_price (float): The original price before discount.
    discount_func (Callable): A function that applies a discount to the base price.

    Returns:
    float: The final price after discount.
    """
    return discount_func(user, base_price)

@check_permissions("get_discount_function")
def get_discount_function(user: Dict[str, str], customer_type: str) -> Callable[[Dict[str, str], float], float]:
    """
    Return a discount function based on customer type.

    Parameters:
    user (Dict[str, str]): The user retrieving the discount function.
    customer_type (str): The type of customer (e.g., 'regular', 'member').

    Returns:
    Callable[[Dict[str, str], float], float]: A discount function.
    """
    def member_discount(user: Dict[str, str], price: float) -> float:
        return price * (1 - config["premium_discount"])

    def regular_discount(user: Dict[str, str], price: float) -> float:
        return price * (1 - config["base_discount"])

    if customer_type == 'member':
        return member_discount
    else:
        return regular_discount

import argparse

# Create ArgumentParser object
parser = argparse.ArgumentParser(description="Bookstore CLI")

# Add arguments
parser.add_argument("--user", required=True, help="User name")
parser.add_argument("--role",  required=True, choices=["admin", "user"], help="User role")
parser.add_argument("--base-price",  required=True, type=float, help="Base price for calculations")
parser.add_argument("--discount-type",  required=False, choices=["10", "20"], help="Type of discount (10 or 20)")

# Parse arguments from command line
args = parser.parse_args()

# Simulate user dictionary based on input
user = {"name": args.user, "role": args.role}

# Handle commands
if args.discount_type:
    if args.discount_type == "10":
        try:
            final_price = calculate_price(user, args.base_price, discount_10)
            print(f"Final price after 10% discount for {user['name']}: ${final_price:.2f}")
        except PermissionError as e:
            print(e)
    elif args.discount_type == "20":
        try:
            final_price = calculate_price(user, args.base_price, discount_20)
            print(f"Final price after 20% discount for {user['name']}: ${final_price:.2f}")
        except PermissionError as e:
            print(e)
elif args.role == "admin":
    try:
        discount_func = get_discount_function(user, 'member')
        final_price = discount_func(user, args.base_price)
        print(f"Final price with premium discount for {user['name']}: ${final_price:.2f}")
    except PermissionError as e:
        print(e)
elif args.role == "user":
    try:
        discount_func = get_discount_function(user, 'regular')
        final_price = discount_func(user, args.base_price)
        print(f"Final price with regular discount for {user['name']}: ${final_price:.2f}")
    except PermissionError as e:
        print(e)
else:
    print("Invalid command or missing required arguments. Use --help for usage information.")

