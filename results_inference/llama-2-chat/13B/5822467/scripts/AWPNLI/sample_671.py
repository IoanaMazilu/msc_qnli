books_in_bin_premise = 41.0
books_removed_premise = 2.0
books_sold_premise = 33.0
books_hypothesis = 3.0

# compute the number of books left in the bin after removing 2 books
books_left_premise = books_in_bin_premise - books_removed_premise

# check if the number of books in the hypothesis is less than or equal to the number of books left in the bin
if books_hypothesis <= books_left_premise:
    # if the hypothesis value is less than or equal to the premise value, we can infer entailment
    label = "entailment"
elif books_hypothesis > books_left_premise:
    # if the hypothesis value is greater than the premise value, we can infer contradiction
    label = "contradiction"
else:
    # if the hypothesis value is the same as the premise value, we cannot infer entailment or contradiction
    label = "neutral"

print(label)
