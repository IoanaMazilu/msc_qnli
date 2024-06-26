james_capital_premise = 600
james_capital_hypothesis = 300

# the hypothesis talks about James' capital, referenced also in the premise
if james_capital_hypothesis <= james_capital_premise:
    # check if the hypothesis value contradicts the estimate of less than 'james_capital_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for James' capital
    # any value of James' capital less than 'james_capital_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
