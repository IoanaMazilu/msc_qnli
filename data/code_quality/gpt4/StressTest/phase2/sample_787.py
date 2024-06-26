income_spent_petrol_premise = 60
income_spent_petrol_hypothesis = 30

# the hypothesis refers to the percentage of income Bhanu spends on petrol, mentioned in the premise
if income_spent_petrol_hypothesis >= income_spent_petrol_premise:
    # check if the percentage in the hypothesis contradicts the estimate of less than 'income_spent_petrol_premise' percentage in the premise
    label = "contradiction"
else:
    # any percentage less than 'income_spent_petrol_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
