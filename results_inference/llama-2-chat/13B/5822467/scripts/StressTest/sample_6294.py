jones_money_premise = 40
jones_money_hypothesis = 60

# the hypothesis refers to the percentage of money given by Jones to his wife
if jones_money_hypothesis <= jones_money_premise:
    # check if the hypothesis value contradicts the estimate of 'jones_money_premise'
    label = "contradiction"
elif jones_money_hypothesis > jones_money_premise:
    # check if the hypothesis value entails the premise
    label = "entailment"
else:
    # the premise gives only an estimate for the percentage of money given by Jones to his wife
    # any percentage less than 60% is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
