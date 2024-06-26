# fraction of sum Anup was asked to find in premise and hypothesis
anup_fraction_premise = 7/12
anup_fraction_hypothesis = 7/12

# the hypothesis refers to the fraction of the sum of money Anup was asked to find in the premise
if anup_fraction_hypothesis >= anup_fraction_premise:
    # check if the estimate of 'anup_fraction_hypothesis' contradicts the fraction in the premise
    label = "contradiction"
else:
    # the premise gives an exact fraction of the sum Anup was asked to find
    # any fraction less than 'anup_fraction_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
