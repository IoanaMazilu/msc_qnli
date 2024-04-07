# Premise: The sum of ages of Aswin, Sachin and Sumesh is 93 years.
# Hypothesis: The sum of ages of Aswin, Sachin and Sumesh is more than 43 years.
# Golden Label: entailment

sum_ages_premise = 93
sum_ages_hypothesis = 43

# The hypothesis also talks about the sum of the ages of Aswin, Sachin and Sumesh
if sum_ages_premise < sum_ages_hypothesis:
    # Check if the sum of ages mentioned in the premise is less than the sum of ages in the hypothesis
    label = "contradiction"
else:
    # If the sum of ages in the premise is greater or equal to the sum of ages in the hypothesis, we can infer entailment
    label = "entailment"

print(label)

