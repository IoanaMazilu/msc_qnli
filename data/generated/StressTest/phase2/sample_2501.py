# Premise: Aamir saves 32% of his monthly salary.
# Hypothesis: Aamir saves 12% of his monthly salary.
# Golden Label: contradiction

aamir_savings_premise = 32
aamir_savings_hypothesis = 12

# the hypothesis refers to Aamir's savings percentage, mentioned in the premise as well
if aamir_savings_hypothesis != aamir_savings_premise:
    # check if the savings percentage in hypothesis contradicts the savings percentage reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

