# # Conditional Statements: 
# #   Use if/else to execute code based on conditions.
# # Exception Handling: 
# #   Use try/except to handle errors without crashing your program.
# # Switch/Case Logic with Dictionary Mapping: 
# #   Use dictionaries to map keys to functions for switch-like behavior.


# # if(condition == boolean):
#     # run code
# #  else if()
#     # run else statemet

# # x = 23

# # if x > 87:
# #     print("Hello")
# # Functions as First Class Objects
# # 1. Assigned to a variable
# # 2. Passed as argauments to other functions
# # 3. Returned from other functions


# # Decorators

# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper

# @my_decorator
# def say_hello():
#     print("Hello!")


# @my_decorator
# def new_func():
#     @my_decorator
#     def func():
#         pass
#     pass

# new_func()


# Config Object

config = {
    "base_discount": 0.23,
    "premium_discount": 0.40,
    "permission_levels" : {
        "admin" : ["apply_discount", "calculate_price", "get_discount_function"],
        "user": ["calculate_price", "get_discount_function"]
    }
}

def check_permissions(permission):
    """
    Decorator to check if the user has the required permission.

    Parameters:
    permission (str): The required permission.

    Returns:
    Callable: The wrapped function if permission is granted.
    """
    
    def decorator(func):
        def wrapper(user, *args, **kwargs):
            # Add some logic
            user_role = user.get("role")
            if user_role is None:
                raise ValueError("User is not defined.")
            
            user_permissions = config["permission_levels"].get(user_role, [])
            if permission in user_permissions:
                return func(user, *args, **kwargs)
            else:
                raise PermissionError(f"User '{user['name']}' does not have permission to execute '{func.__name__}'")
        return wrapper
    return decorator
    
@check_permissions("apply_discount")
def discount_10(user, price):
    return price * 0.9

@check_permissions("apply_discount")
def discount_20(user, price):
    return price * 0.8

@check_permissions("calculate_price")
def calculate_price(user, base_price, disc_func):
    return disc_func(user, base_price)

@check_permissions("get_discount_function")
def get_discount_function(user, customer_type):

    def premium_account(user, price):
        return price * (1 - config["premium_discount"])
    
    def regular_account(user, price):
        return price * (1 - config["base_discount"])
    
    if customer_type == "member":
        return premium_account
    else:
        return regular_account
        

import argparse
 

parser = argparse.ArgumentParser(description="Bookstore CLI")

parser.add_argument("--user")
parser.add_argument("--base-price", type=float)
parser.add_argument("--role", choices=["admin", "user"])
parser.add_argument("--discount-type", choices=["10", "20"])

args = parser.parse_args()

user = {
    "name": args.user,
    "role": args.role
}

if args.discount_type:
    if args.discount_type == "10":
        try:
            final_price = calculate_price(user, args.base_price, discount_10)
            print(f"Final price after 10% discount for {user['name']}: Kes{final_price:.2f}")
        except PermissionError as e:
            print(e)
    elif args.discount_type == "20":
        try:
            final_price = calculate_price(user, args.base_price, discount_20)
            print(f"Final price after 10% discount for {user['name']}: Kes{final_price:.2f}")

        except PermissionError as e:
            print(e)
elif args.role == "admin":
        try:
            disc_func = get_discount_function(user, "member")
            final_price = disc_func(user, args.base_price)
            print(f"Final price with premium discount for {user['name']}: Kes{final_price:.2f}")
        except PermissionError as e:
            print(e)
elif args.role == "user":
        try:
            disc_func = get_discount_function(user, "regular")
            final_price = disc_func(user, args.base_price)
            print(f"Final price with discount for {user['name']}: Kes{final_price:.2f}")
        except PermissionError as e:
            print(e)
else:
    print("Invalid command or missing required fields")
