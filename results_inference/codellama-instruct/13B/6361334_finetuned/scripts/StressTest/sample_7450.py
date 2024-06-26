income_premise = 0.8
income_hypothesis = 0.3
petrol_premise = 0.12
petrol_hypothesis = 0.12
house_rent_premise = 0.12
house_rent_hypothesis = 0.12
food_premise = 0.68
food_hypothesis = 0.68

# the hypothesis refers to the percentage of income spent on petrol, house rent, and food, which are also mentioned in the premise
if income_hypothesis <= income_premise:
    # check if the hypothesis value contradicts the estimate of less than 'income_premise'
    label = "contradiction"
elif petrol_hypothesis!= petrol_premise:
    # check if the percentage of income spent on petrol in the hypothesis contradicts the percentage mentioned in the premise
    label = "contradiction"
elif house_rent_hypothesis!= house_rent_premise:
    # check if the percentage of income spent on house rent in the hypothesis contradicts the percentage mentioned in the premise
    label = "contradiction"
elif food_hypothesis!= food_premise:
    # check if the percentage of income spent on food in the hypothesis contradicts the percentage mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
