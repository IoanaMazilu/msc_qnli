income_petrol_premise = 30
income_petrol_hypothesis = 30

# the hypothesis refers to the percentage of income Bhanu spends on petrol, which is also mentioned in the premise
if income_petrol_hypothesis <= income_petrol_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise gives an exact percentage for the income spent on petrol
    # any percentage greater than 'income_petrol_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
