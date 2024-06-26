shelves_premise = 150.0
books_per_shelf_premise = 15.0
total_books_premise = shelves_premise * books_per_shelf_premise

books_hypothesis = 2250.0

# Check if the total number of books in the hypothesis contradicts the premise
if books_hypothesis!= total_books_premise:
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
