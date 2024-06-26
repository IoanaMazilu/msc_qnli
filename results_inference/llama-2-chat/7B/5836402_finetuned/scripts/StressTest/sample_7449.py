income_spent_petrol_premise = 30
income_spent_petrol_hypothesis = 80

# the hypothesis refers to the percentage of income spent on petrol, which is also mentioned in the premise
if income_spent_petrol_hypothesis >= income_spent_petrol_premise:
    # check if the estimate of 'income_spent_petrol_hypothesis' contradicts the percentage of income spent on petrol in the premise
    label = "contradiction"
elif income_spent_petrol_hypothesis < income_spent_petrol_premise:
    # if the percentage of income spent on petrol in the hypothesis is less than the percentage in the premise, it is entailed
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)
