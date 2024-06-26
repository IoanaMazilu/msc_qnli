petrol_income_bhanu_premise = 80
petrol_income_bhanu_hypothesis = 30
house_rent_bhanu_premise = 12
house_rent_bhanu_hypothesis = 12
food_bhanu_premise = 12
food_bhanu_hypothesis = 12

# the hypothesis refers to the percentage of income spent on petrol, house rent, and food
if petrol_income_bhanu_hypothesis >= petrol_income_bhanu_premise:
    # check if the hypothesis value contradicts the premise value for petrol income
    label = "contradiction"
elif house_rent_bhanu_hypothesis!= house_rent_bhanu_premise:
    # check if the hypothesis value contradicts the premise value for house rent
    label = "contradiction"
elif food_bhanu_hypothesis!= food_bhanu_premise:
    # check if the hypothesis value contradicts the premise value for food
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
