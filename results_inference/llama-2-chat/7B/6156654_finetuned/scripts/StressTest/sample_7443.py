petrol_spent_premise = 30
petrol_spent_hypothesis = 60
house_rent_premise = 14
house_rent_hypothesis = 14
food_premise = 100 - (petrol_spent_premise + house_rent_premise)
food_hypothesis = 100 - (petrol_spent_hypothesis + house_rent_hypothesis)

# the hypothesis refers to the same percentages of income spent on petrol, house rent and food as the premise
if petrol_spent_hypothesis <= petrol_spent_premise:
    # check if the hypothesis value contradicts the premise value for petrol spending
    label = "contradiction"
elif house_rent_hypothesis!= house_rent_premise:
    # check if the hypothesis value contradicts the premise value for house rent
    label = "contradiction"
elif food_hypothesis!= food_premise:
    # check if the hypothesis value contradicts the premise value for food
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
