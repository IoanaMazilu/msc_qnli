petrol_income_premise = 30
petrol_income_hypothesis = 80
house_rent_premise = 12
house_rent_hypothesis = 12
food_premise = 100 - (petrol_income_premise + house_rent_premise)
food_hypothesis = 100 - (petrol_income_hypothesis + house_rent_hypothesis)

# the hypothesis refers to the percentage of income spent on petrol, house rent and food, which are also mentioned in the premise
if petrol_income_hypothesis <= petrol_income_premise:
    # check if the hypothesis value contradicts the premise value of petrol income
    label = "entailment"
elif house_rent_hypothesis!= house_rent_premise:
    # check if the hypothesis value contradicts the premise value of house rent
    label = "contradiction"
elif food_hypothesis!= food_premise:
    # check if the hypothesis value contradicts the premise value of food
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "neutral"

print(label)
