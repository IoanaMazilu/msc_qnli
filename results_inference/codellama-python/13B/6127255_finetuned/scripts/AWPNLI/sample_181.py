books_on_shelf_premise = 38.0
books_added_premise = 10.0
books_on_shelf_hypothesis = 52.0

# the hypothesis refers to the number of books on the shelf, which is also mentioned in the premise
# compute the total number of books on the shelf in the premise
total_books_premise = books_on_shelf_premise + books_added_premise
if books_on_shelf_hypothesis!= total_books_premise:
    # check if the number of books in the hypothesis contradicts the number of books from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
