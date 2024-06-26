# Define variables for the premise
book_shelves_premise = 150.0
books_per_shelf_premise = 15.0
total_books_premise = book_shelves_premise * books_per_shelf_premise

# Define variables for the hypothesis
total_books_hypothesis = 2250.0

# Check if the total number of books in the hypothesis is greater than the total number of books in the premise
if total_books_hypothesis > total_books_premise:
    label = "entailment"
else:
    label = "contradiction"

print(label)
