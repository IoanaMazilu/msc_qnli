income_premise = 0.3
income_hypothesis = 0.6
petrol_premise = 0.14
petrol_hypothesis = 0.14
house_rent_premise = 0.14
house_rent_hypothesis = 0.14
food_premise = 0.56
food_hypothesis = 0.56

# the hypothesis refers to the percentage of income spent on petrol, house rent and food
if income_hypothesis <= income_premise:
    # check if the hypothesis value contradicts the estimate of more than 'income_premise'
    label = "contradiction"
elif petrol_hypothesis!= petrol_premise:
    # check if the percentage of income spent on petrol in the hypothesis contradicts the percentage of income spent on petrol reported in the premise
    label = "contradiction"
elif house_rent_hypothesis!= house_rent_premise:
    # check if the percentage of income spent on house rent in the hypothesis contradicts the percentage of income spent on house rent reported in the premise
    label = "contradiction"
elif food_hypothesis!= food_premise:
    # check if the percentage of income spent on food in the hypothesis contradicts the percentage of income spent on food reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
