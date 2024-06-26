petrol_income_premise = 30
petrol_income_hypothesis = 80
house_rent_premise = 12
house_rent_hypothesis = 12
food_balance_premise = 80 - (petrol_income_premise + house_rent_premise)
food_balance_hypothesis = 80 - (petrol_income_hypothesis + house_rent_hypothesis)

# the hypothesis talks about the percentage of income spent on petrol, house rent and food, which are also mentioned in the premise
if petrol_income_hypothesis <= petrol_income_premise:
    # check if the hypothesis value for petrol income is less than or equal to the premise value
    label = "entailment"
elif house_rent_hypothesis!= house_rent_premise:
    # check if the house rent percentage in the hypothesis is different from the house rent percentage in the premise
    label = "contradiction"
elif food_balance_hypothesis!= food_balance_premise:
    # check if the food balance percentage in the hypothesis is different from the food balance percentage in the premise
    label = "contradiction"
else:
    # if the hypothesis values and premise values are the same, it is neutral
    label = "neutral"

print(label)
