books_on_shelf_premise = 38.0
books_taken_premise = 10.0
books_on_shelf_hypothesis = 26.0

# the hypothesis refers to the number of books on the shelf, which is also mentioned in the premise
# compute the remaining number of books on the shelf in the premise
remaining_books_premise = books_on_shelf_premise - books_taken_premise
if books_on_shelf_hypothesis!= remaining_books_premise:
    # check if the number of books on the shelf in the hypothesis contradicts the number of books from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
