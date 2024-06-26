income_spent_petrol_premise = 30
income_spent_petrol_hypothesis = 60
income_spent_house_rent_premise = 14
income_spent_house_rent_hypothesis = 14
income_remaining_premise = 100 - income_spent_petrol_premise - income_spent_house_rent_premise
income_remaining_hypothesis = 100 - income_spent_petrol_hypothesis - income_spent_house_rent_hypothesis

# the hypothesis refers to the percentage of income spent on petrol and house rent, as well as the remaining income
if income_spent_petrol_hypothesis >= income_spent_petrol_premise:
    # check if the percentage of income spent on petrol in the hypothesis contradicts the premise
    label = "contradiction"
elif income_spent_house_rent_hypothesis!= income_spent_house_rent_premise:
    # check if the percentage of income spent on house rent in the hypothesis contradicts the premise
    label = "contradiction"
elif income_remaining_hypothesis!= income_remaining_premise:
    # check if the remaining income in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
