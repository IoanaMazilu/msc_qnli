# Premise: Rahim bought 27 books for Rs.
# Hypothesis: Rahim bought less than 67 books for Rs.
# Golden Label: entailment

books_bought_premise = 27
books_bought_hypothesis = 67

# the hypothesis talks about the number of books Rahim bought, which is also mentioned in the premise
if books_bought_premise >= books_bought_hypothesis:
    # check if the number of books bought in the premise contradicts the estimate of less than 'books_bought_hypothesis'
    label = "contradiction"
else:
    # if the number of books bought in the premise is less than 'books_bought_hypothesis', it is consistent with the hypothesis, thus we can infer entailment
    label = "entailment"

print(label)

