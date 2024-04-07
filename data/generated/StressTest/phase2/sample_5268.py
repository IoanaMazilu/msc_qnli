# Premise: Aamir saves 32% of his monthly salary.
# Hypothesis: Aamir saves less than 82% of his monthly salary.
# Golden Label: entailment

savings_percentage_premise = 32
savings_percentage_hypothesis = 82

# the hypothesis refers to the percentage of salary saved by Aamir mentioned in the premise
if savings_percentage_premise >= savings_percentage_hypothesis:
    # check if the 'savings_percentage_premise' contradicts the fact that Aamir saves less than 'savings_percentage_hypothesis'
    label = "contradiction"
else:
    # if the savings percentage in the premise is less than the one in the hypothesis, we can infer entailment
    label = "entailment"

print(label)

