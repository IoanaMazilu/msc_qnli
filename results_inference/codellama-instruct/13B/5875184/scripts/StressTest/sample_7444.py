income_premise = 0.6
income_hypothesis = 0.3
petrol_premise = 0.14
petrol_hypothesis = 0.14
house_rent_premise = 0.14
house_rent_hypothesis = 0.14
food_premise = 0.14
food_hypothesis = 0.14

# the hypothesis refers to the percentage of income spent on petrol, house rent, and food
if income_hypothesis <= income_premise:
    # check if the hypothesis value contradicts the estimate of less than 'income_premise'
    label = "contradiction"
elif petrol_hypothesis!= petrol_premise:
    # check if the number of sold pies in the hypothesis contradicts the number of sold pies reported in the premise
    label = "contradiction"
elif house_rent_hypothesis!= house_rent_premise:
    # check if the number of sold pies in the hypothesis contradicts the number of sold pies reported in the premise
    label = "contradiction"
elif food_hypothesis!= food_premise:
    # check if the number of sold pies in the hypothesis contradicts the number of sold pies reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
