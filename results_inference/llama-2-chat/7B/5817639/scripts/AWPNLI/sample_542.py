books_premise = 54.0
books_hypothesis = 31.0

# compare the number of books left in the library between the premise and the hypothesis
if books_hypothesis == books_premise:
    # if the number of books left in the library is the same in both the premise and the hypothesis, we can infer entailment
    label = "entailment"
else:
    # if the number of books left in the library is different in the hypothesis and the premise, we can infer contradiction
    label = "contradiction"

print(label)
