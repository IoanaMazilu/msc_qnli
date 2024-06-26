petrol_expense_premise = 80
petrol_expense_hypothesis = 30
house_rent_expense_premise = 12
house_rent_expense_hypothesis = 12

# the hypothesis refers to the percentage of income Bhanu spends on petrol and house rent, mentioned also in the premise
if petrol_expense_premise < petrol_expense_hypothesis:
    # check if the percentage of petrol expense in the hypothesis contradicts that in the premise
    label = "contradiction"
elif house_rent_expense_premise != house_rent_expense_hypothesis:
    # check if the percentage of house rent expense in the hypothesis contradicts that in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
