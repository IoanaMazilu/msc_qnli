income_premise = 30
petrol_premise = 12
house_rent_premise = 12
food_premise = 12

income_hypothesis = 30
petrol_hypothesis = 12
house_rent_hypothesis = 12
food_hypothesis = 12

# the hypothesis refers to the percentage of income spent on petrol, house rent, and food
if petrol_hypothesis > petrol_premise:
    # check if the hypothesis value contradicts the estimate of 'petrol_premise'
    label = "contradiction"
elif house_rent_hypothesis > house_rent_premise:
    # check if the hypothesis value contradicts the estimate of 'house_rent_premise'
    label = "contradiction"
elif food_hypothesis > food_premise:
    # check if the hypothesis value contradicts the estimate of 'food_premise'
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
