petrol_spent_premise = 30
petrol_spent_hypothesis = 30
house_rent_premise = 12
house_rent_hypothesis = 12
food_balance_premise = 60
food_balance_hypothesis = 60

# the hypothesis refers to the percentage of income spent on petrol, house rent and food as mentioned in the premise
if petrol_spent_hypothesis >= petrol_spent_premise:
    # check if the estimate of 'petrol_spent_hypothesis' contradicts the percentage of petrol spend in the premise
    label = "contradiction"
elif house_rent_hypothesis!= house_rent_premise:
    # check if the percentage of house rent in the hypothesis contradicts the percentage of house rent reported in the premise
    label = "contradiction"
elif food_balance_hypothesis!= food_balance_premise:
    # check if the percentage of food in the hypothesis contradicts the percentage of food reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
