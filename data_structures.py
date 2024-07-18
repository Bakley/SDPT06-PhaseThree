# Type of data structures
# List/array
# # Indexed, Mutable, [] 0(n)

# Tuple
## Ordered, Immutable(the elements are not modified)
## (,)

# Dictionary
## {
#     key: value
## }
# unordered, mutable, the look up condition is always a constant time(0(1))
# import jsonify
# books = []
# def get_single_book(book_id, book_name):
#     book = next((book for book in books if book.id == book_id), None)


#     if book is None:
#         return jsonify({
#             "error": 'Book not found'
#         }), 404
#     return jsonify(book.to_dict()), 200

# Generators and comprehensions
# # A python tool for working with sequence of data 
# # when dealing with large datasets or streams of data
# ### Inbuilt methods to control executions ### #
# next()
# => retrive the next item form the iterable
# send(value)
# => resume the generator and sends the value that can be used to modity state
# throw(type, value=None, traceback=None)
# => raisea an exception
# close()


# List comprehsion

x = []

for item in range(10):
    x.append(item)
print(x)

var_for_list_comp = (item for item in range(20))
print(var_for_list_comp)
