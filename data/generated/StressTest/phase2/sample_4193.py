# Premise: 1000, what is Isabella's capital?
# Hypothesis: 5000, what is Isabella's capital?
# Golden Label: contradiction

capital_premise = 1000
capital_hypothesis = 5000

# The hypothesis is referring to Isabella's capital, also mentioned in the premise
if capital_hypothesis != capital_premise:
    # Check if the amount in the hypothesis contradicts the amount in the premise
    label = "contradiction"
else:
    # If the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)

