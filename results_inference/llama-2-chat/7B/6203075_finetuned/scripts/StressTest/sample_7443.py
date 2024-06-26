petrol_income_premise = 30
petrol_income_hypothesis = 60
house_rent_premise = 14
house_rent_hypothesis = 14
food_premise = 100 - (petrol_income_premise + house_rent_premise)
food_hypothesis = 100 - (petrol_income_hypothesis + house_rent_hypothesis)

# the hypothesis refers to the percentage of income spent on petrol, house rent and food, which are also mentioned in the premise
if petrol_income_hypothesis > petrol_income_premise:
    # check if the percentage of income spent on petrol in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
elif house_rent_hypothesis!= house_rent_premise:
    # check if the percentage of income spent on house rent in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
elif food_hypothesis!= food_premise:
    # check if the percentage of income spent on food in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
