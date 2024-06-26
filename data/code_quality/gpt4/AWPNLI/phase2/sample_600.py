books_on_shelf_premise = 38.0
books_taken_premise = 10.0
books_on_shelf_hypothesis = 28.0

# the hypothesis refers to the number of books left on the shelf, which can be calculated from the premise
# compute the number of books left on the shelf in the premise
books_left_premise = books_on_shelf_premise - books_taken_premise
if books_on_shelf_hypothesis != books_left_premise:
    # check if the number of books left on the shelf in the hypothesis contradicts the number of books left on the shelf from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
