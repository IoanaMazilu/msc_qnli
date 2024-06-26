petrol_income_premise = 30
petrol_income_hypothesis = 30
house_rent_premise = 14
house_rent_hypothesis = 14
food_balance_premise = 56
food_balance_hypothesis = 56

# the hypothesis refers to the same percentage of income spent on petrol, house rent, and food as in the premise
if petrol_income_hypothesis!= petrol_income_premise:
    label = "contradiction"
elif house_rent_hypothesis!= house_rent_premise:
    label = "contradiction"
elif food_balance_hypothesis!= food_balance_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
