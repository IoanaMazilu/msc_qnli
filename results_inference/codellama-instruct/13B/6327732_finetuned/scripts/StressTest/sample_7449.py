income_premise = 100
petrol_premise = 30
house_rent_premise = 12
food_premise = 100 - petrol_premise - house_rent_premise

income_hypothesis = 100
petrol_hypothesis = 80
house_rent_hypothesis = 12
food_hypothesis = 100 - petrol_hypothesis - house_rent_hypothesis

# the hypothesis refers to the percentage of income spent on petrol, house rent, and food
if petrol_hypothesis > petrol_premise:
    # check if the hypothesis value contradicts the percentage of income spent on petrol in the premise
    label = "contradiction"
elif house_rent_hypothesis!= house_rent_premise:
    # check if the hypothesis value contradicts the percentage of income spent on house rent in the premise
    label = "contradiction"
elif food_hypothesis!= food_premise:
    # check if the hypothesis value contradicts the percentage of income spent on food in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
