# Premise: Anup was asked to find the value of 7/12 of a sum of money T.
# Hypothesis: Anup was asked to find the value of more than 7/12 of a sum of money T.
# Golden Label: contradiction

fraction_premise = 7/12
fraction_hypothesis = 7/12

# the hypothesis refers to the fraction of a sum of money mentioned in the premise
if fraction_hypothesis > fraction_premise:
    # check if the fraction in the hypothesis contradicts the fraction of the sum of money in the premise
    label = "contradiction"
elif fraction_hypothesis < fraction_premise:
    # check if the fraction in the hypothesis is less than the fraction mentioned in the premise
    label = "contradiction"
else:
    # the premise gives the exact fraction of the sum of money
    # the hypothesis refers to more than the given fraction which is consistent with the premise, but cannot be explicitly entailed from it
    label = "neutral"

print(label)

