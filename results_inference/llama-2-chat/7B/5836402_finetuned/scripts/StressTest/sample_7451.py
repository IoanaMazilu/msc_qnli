income_spent_petrol_premise = 30
income_spent_petrol_hypothesis = 30
income_spent_house_rent_premise = 12
income_spent_house_rent_hypothesis = 12
income_balance_premise = 100 - income_spent_petrol_premise - income_spent_house_rent_premise
income_balance_hypothesis = 100 - income_spent_petrol_hypothesis - income_spent_house_rent_hypothesis

# the hypothesis refers to the same aspects mentioned in the premise
if income_spent_petrol_premise <= income_spent_petrol_hypothesis:
    # check if the estimate of 'income_spent_petrol_hypothesis' contradicts the number of income spent on petrol in the premise
    label = "contradiction"
elif income_spent_house_rent_hypothesis!= income_spent_house_rent_premise:
    # check if the number of income spent on house rent in the hypothesis contradicts the number of income spent on house rent reported in the premise
    label = "contradiction"
elif income_balance_hypothesis!= income_balance_premise:
    # check if the balance of income in the hypothesis contradicts the balance of income reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
