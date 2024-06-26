income_premise = 30
petrol_premise = 14
house_rent_premise = 14
food_premise = 56

income_hypothesis = 30
petrol_hypothesis = 14
house_rent_hypothesis = 14
food_hypothesis = 56

# the hypothesis refers to the percentage of income spent on petrol, house rent, and food, which are also mentioned in the premise
if petrol_hypothesis > petrol_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif house_rent_hypothesis!= house_rent_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif food_hypothesis!= food_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
