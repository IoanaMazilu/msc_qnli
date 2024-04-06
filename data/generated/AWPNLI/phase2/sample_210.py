# Premise: There were 150.0 book shelves and each book shelf had 15.0 books.
# Hypothesis: 2250.0 books were on the shelves.
# Golden Label: entailment

shelves_premise = 150.0
books_per_shelf_premise = 15.0
total_books_hypothesis = 2250.0

# the hypothesis refers to the total number of books, which are also mentioned in the premise
# compute the total number of books in the premise
total_books_premise = shelves_premise * books_per_shelf_premise
if total_books_hypothesis != total_books_premise:
    # check if the total number of books in the hypothesis contradicts the total number of books from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

