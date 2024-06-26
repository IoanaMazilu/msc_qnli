income_petrol_premise = 80
income_petrol_hypothesis = 30

# the hypothesis refers to the percentage of income Bhanu spends on petrol, which is also mentioned in the premise
if income_petrol_hypothesis >= income_petrol_premise:
    # check if the percentage of income spent on petrol in the hypothesis contradicts the estimate of less than 'income_petrol_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of income spent on petrol
    # any percentage less than 'income_petrol_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
