petrol_spending_premise = 30
petrol_spending_hypothesis = 80
rent_spending_premise = 12
rent_spending_hypothesis = 12

# the hypothesis refers to the percentage of income Bhanu spends on petrol, house rent and food, mentioned in the premise
if petrol_spending_hypothesis < petrol_spending_premise:
    # check if the estimate of 'petrol_spending_hypothesis' contradicts the percentage of petrol spending in the premise
    label = "contradiction"
elif rent_spending_hypothesis!= rent_spending_premise:
    # check if the percentage of rent spending in the hypothesis contradicts the percentage of rent spending reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
