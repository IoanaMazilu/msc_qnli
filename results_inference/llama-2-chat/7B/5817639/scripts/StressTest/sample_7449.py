petrol_spending_premise = 30
petrol_spending_hypothesis = 80
house_rent_premise = 12
house_rent_hypothesis = 12
food_spending_premise = float(petrol_spending_premise * 0.7)
food_spending_hypothesis = float(petrol_spending_hypothesis * 0.7)

# the hypothesis refers to the amount of money spent on petrol, house rent, and food, as mentioned in the premise
if petrol_spending_premise <= petrol_spending_hypothesis:
    # check if the estimate of 'petrol_spending_hypothesis' contradicts the amount of petrol spending in the premise
    label = "contradiction"
elif house_rent_hypothesis!= house_rent_premise:
    # check if the number of rent paid in the hypothesis contradicts the number of rent paid reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
