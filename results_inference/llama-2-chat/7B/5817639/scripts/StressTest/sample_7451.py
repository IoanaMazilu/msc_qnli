petrol_spending_premise = 0.3
petrol_spending_hypothesis = 0.4
house_rent_premise = 0.12
house_rent_hypothesis = 0.12
food_premise = 0.6
food_hypothesis = 0.6

# the hypothesis refers to the percentage of income spent on petrol, house rent, and food, as stated in the premise
if petrol_spending_hypothesis <= petrol_spending_premise:
    # check if the estimate of 'petrol_spending_hypothesis' contradicts the percentage of income spent on petrol in the premise
    label = "contradiction"
elif house_rent_hypothesis!= house_rent_premise:
    # check if the number of house rent in the hypothesis contradicts the number of house rent reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
