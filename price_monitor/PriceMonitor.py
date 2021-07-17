## Class that analyzes products and checks if the price has changed or if the value is below a user's threshold
# Stores:
#   - Array of user's, with no min and no max
#   - Array of product's, with no max but at least one
#
# Functions:
#   - Constructor that receives products and users to store in the class attributes.
#   - Functions to read users and products files, and convert them into Product and User classes.
#   - Function that calls to SeleniumController class and analyzes if the product has changed