# Premise: A box of books weighs 42.0 pounds and each book weighs 3.0 pounds.
# Hypothesis: 14.0 books are there in the box.
# Golden Label: entailment

box_weight_premise = 42.0
book_weight_premise = 3.0
books_hypothesis = 14.0

# the hypothesis refers to the number of books, which can be computed from the premise
# compute the number of books in the premise
books_premise = box_weight_premise / book_weight_premise
if books_hypothesis != books_premise:
    # check if the number of books in the hypothesis contradicts the number of books from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

