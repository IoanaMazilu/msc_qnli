books_weight_premise = 42.0
books_weight_hypothesis = 14.0

# the hypothesis refers to the number of books in the box, which can be calculated from the premise
# compute the total weight of books in the premise
total_books_weight_premise = books_weight_premise * books_weight_hypothesis

# the hypothesis value is less than the total weight of books in the premise
if books_weight_hypothesis > total_books_weight_premise:
    # check if the number of books in the hypothesis contradicts the total weight of books in the premise
    label = "contradiction"
else:
    # if the number of books in the hypothesis does not contradict the total weight of books in the premise
    # then we can infer entailment
    label = "entailment"

print(label)
