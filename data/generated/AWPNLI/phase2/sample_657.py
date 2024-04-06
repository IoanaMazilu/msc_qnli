# Premise: A box of books weighs 42 pounds, and each book weighs 3 pounds.
# Hypothesis: 130.0 books are there in the box.
# Golden Label: contradiction

box_weight_premise = 42
book_weight_premise = 3
books_in_box_hypothesis = 130.0

# the hypothesis refers to the total number of books in the box, which is indirectly mentioned in the premise
# compute the total number of books in the premise
books_in_box_premise = box_weight_premise / book_weight_premise
if books_in_box_hypothesis != books_in_box_premise:
    # check if the number of books in the box in the hypothesis contradicts the number of books in the box from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

