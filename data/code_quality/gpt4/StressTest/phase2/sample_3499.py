income_spent_on_petrol_premise = 80
income_spent_on_petrol_hypothesis = 30
income_spent_on_rent = 20

# the hypothesis refers to the percentage of income spent on petrol and rent, which is also mentioned in the premise
if income_spent_on_petrol_hypothesis >= income_spent_on_petrol_premise:
    # check if the hypothesis value contradicts the estimate of less than 'income_spent_on_petrol_premise'
    label = "contradiction"
elif income_spent_on_rent != income_spent_on_rent:
    # check if the percentage of income spent on rent in the hypothesis contradicts the percentage of income spent on rent in the premise
    label = "contradiction"
else:
    # the hypothesis values and estimates do not contradict the premise ones, but they also do not fully entail the premise
    label = "neutral"

print(label)
