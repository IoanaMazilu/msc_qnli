income_spent_on_petrol_premise = 80
income_spent_on_petrol_hypothesis = 30

# the hypothesis talks about the percentage of income spent on petrol, referenced also in the premise
if income_spent_on_petrol_hypothesis >= income_spent_on_petrol_premise:
    # check if the hypothesis value contradicts the estimate of less than 'income_spent_on_petrol_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of income spent on petrol
    # any percentage of income less than 'income_spent_on_petrol_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
