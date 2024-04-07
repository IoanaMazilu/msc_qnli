# Premise: Anup was asked to find the value of 7/12 of a sum of money Q.
# Hypothesis: Anup was asked to find the value of more than 4/12 of a sum of money Q.
# Golden Label: entailment

value_premise = 7/12
value_hypothesis = 4/12

# the hypothesis refers to the value Anup was asked to find in the premise
if value_hypothesis >= value_premise:
    # check if the hypothesis value contradicts the exact value asked in the premise
    label = "contradiction"
elif value_hypothesis < value_premise:
    # since the hypothesis value is less than the premise value, it is entailed
    label = "entailment"

print(label)

