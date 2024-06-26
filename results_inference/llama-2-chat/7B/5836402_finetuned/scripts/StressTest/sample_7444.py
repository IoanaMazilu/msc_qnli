income_spent_on_petrol_premise = 60
income_spent_on_petrol_hypothesis = 30

# the hypothesis refers to the percentage of income spent on petrol, which is also mentioned in the premise
if income_spent_on_petrol_hypothesis >= income_spent_on_petrol_premise:
    # check if the hypothesis value contradicts the estimate of less than 'income_spent_on_petrol_premise'
    label = "contradiction"
elif income_spent_on_petrol_hypothesis < income_spent_on_petrol_premise:
    # the premise gives only an estimate for the percentage of income spent on petrol
    # any percentage of income less than 'income_spent_on_petrol_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
