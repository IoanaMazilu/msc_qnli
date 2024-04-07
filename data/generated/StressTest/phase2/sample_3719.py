# Premise: Alka bought 15 books for Rs.
# Hypothesis: Alka bought 75 books for Rs.
# Golden Label: contradiction

books_bought_premise = 15
books_bought_hypothesis = 75

# the hypothesis refers to the number of books bought by Alka mentioned in the premise
if books_bought_premise == books_bought_hypothesis:
    # check if the number of 'books_bought_hypothesis' is same as the number of books bought in the premise
    label = "entailment"
else:
    # if the number of books bought in the hypothesis does not match the actual number of books bought reported in the premise, it's a contradiction
    label = "contradiction"

print(label)

