# Premise: Rahim bought 50 books for Rs.
# Hypothesis: Rahim bought 80 books for Rs.
# Golden Label: contradiction

books_bought_premise = 50
books_bought_hypothesis = 80

# the hypothesis refers to the number of books bought by Rahim mentioned in the premise
if books_bought_premise != books_bought_hypothesis:
    # check if the number of books bought in the hypothesis contradicts the number of books bought in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

