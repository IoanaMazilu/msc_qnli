petrol_income_premise = 80
petrol_income_hypothesis = 30
house_rent_premise = 12
house_rent_hypothesis = 12
food_premise = 100 - (petrol_income_premise + house_rent_premise)
food_hypothesis = 100 - (petrol_income_hypothesis + house_rent_hypothesis)

# the hypothesis talks about the percentage of income spent on petrol, house rent and food
if petrol_income_hypothesis > petrol_income_premise:
    # check if the hypothesis value contradicts the premise's estimate of petrol income
    label = "contradiction"
elif house_rent_hypothesis!= house_rent_premise:
    # check if the hypothesis value contradicts the premise's estimate of house rent
    label = "contradiction"
elif food_hypothesis!= food_premise:
    # check if the hypothesis value contradicts the premise's estimate of food
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
