# Premise: Rahim bought 65 books for Rs.
# Hypothesis: Rahim bought less than 65 books for Rs.
# Golden Label: contradiction

books_bought_premise = 65
books_bought_hypothesis = 65

# The hypothesis refers to the number of books bought by Rahim, which is also mentioned in the premise
if books_bought_hypothesis >= books_bought_premise:
    # check if the hypothesis value contradicts the 'less than' condition in the hypothesis
    label = "contradiction"
else:
    # if the hypothesis value is less than the number of books bought in the premise, we can infer entailment
    label = "entailment"

print(label)

