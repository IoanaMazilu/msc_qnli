# Define variables with representative names for the numerical entities in both inputs
books_premise = 14.0
weight_book_premise = 3.0
weight_box_premise = 42.0

# Extract all quantities as valid numbers (integers or floats)
total_weight_premise = weight_book_premise * books_premise

# Use brief comments to explain what comparison you do between the defined variables
# Do not use their values in the comments
if total_weight_premise == weight_box_premise:
    # Check if the total weight of books in the box from the premise is equal to the weight of the box
    label = "entailment"
else:
    # If the total weight of books in the box from the premise is not equal to the weight of the box, we can infer contradiction
    label = "contradiction"

print(label)
