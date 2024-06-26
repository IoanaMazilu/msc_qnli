petrol_spending_premise = 30
petrol_spending_hypothesis = 60
scooter_rent_premise = 14
scooter_rent_hypothesis = 14
food_spending_premise = 100 - petrol_spending_premise - scooter_rent_premise # assuming 100% of income is spent on food
food_spending_hypothesis = 100 - petrol_spending_hypothesis - scooter_rent_hypothesis # assuming 100% of income is spent on food

# the hypothesis refers to the percentage of income Bhanu spends on petrol, scooter rent and food, mentioned in the premise
if petrol_spending_hypothesis < petrol_spending_premise:
    # check if the estimate of 'petrol_spending_hypothesis' contradicts the percentage of petrol spending in the premise
    label = "contradiction"
elif scooter_rent_hypothesis!= scooter_rent_premise:
    # check if the percentage of scooter rent in the hypothesis contradicts the percentage of scooter rent reported in the premise
    label = "contradiction"
elif food_spending_hypothesis!= food_spending_premise:
    # check if the percentage of food spending in the hypothesis contradicts the percentage of food spending reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
