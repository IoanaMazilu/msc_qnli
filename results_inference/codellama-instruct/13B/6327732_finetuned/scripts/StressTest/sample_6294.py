money_jones_had_premise = 40
money_jones_had_hypothesis = 60

# the hypothesis refers to the percentage of money given by Jones to his wife
if money_jones_had_hypothesis >= money_jones_had_premise:
    # check if the hypothesis value contradicts the percentage of money given by Jones in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the percentage of money given by Jones to his wife
    # any percentage less than'money_jones_had_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
