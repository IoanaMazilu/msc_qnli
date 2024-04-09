books_premise = 42.0 / 3.0  # calculate the number of books in the premise
books_hypothesis = 14.0

# compare the number of books in the hypothesis with the estimated number of books in the premise
if books_hypothesis!= books_premise:
    # if the number of books in the hypothesis contradicts the number of books in the premise, the label is contradiction
    label = "contradiction"
else:
    # if the number of books in the hypothesis and the premise are the same, the label is entailment
    label = "entailment"

print(label)
