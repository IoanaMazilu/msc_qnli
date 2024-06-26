books_bargin_premise = 41.0
books_sold_premise = 33.0
books_hypothesis = 3.0

# compare the number of books in the bargin bin before and after the sortation
if books_bargin_premise - books_sold_premise!= books_hypothesis:
    # check if the number of books in the bargin bin after sortation contradicts the hypothesis
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
