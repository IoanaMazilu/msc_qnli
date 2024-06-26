books_premise = 54.0
books_hypothesis = 34.0

# compare the number of books in the hypothesis to the number of books in the premise
if books_hypothesis >= books_premise:
    # if the number of books in the hypothesis is greater than or equal to the number of books in the premise, we can infer entailment
    label = "entailment"
elif books_hypothesis - books_premise == 0:
    # if the number of books in the hypothesis is equal to the number of books in the premise, we can infer neutrality
    label = "neutral"
else:
    # if the number of books in the hypothesis is less than the number of books in the premise, we can infer contradiction
    label = "contradiction"

print(label)
