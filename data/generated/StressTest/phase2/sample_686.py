# Premise: Jones gave 40% of the money he had to his wife.
# Hypothesis: Jones gave less than 40% of the money he had to his wife.
# Golden Label: contradiction

percentage_given_premise = 40
percentage_given_hypothesis = 40

# the hypothesis refers to the percentage of money given by Jones to his wife, as mentioned in the premise
if percentage_given_hypothesis >= percentage_given_premise:
    # check if the hypothesis value contradicts the percentage given in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

