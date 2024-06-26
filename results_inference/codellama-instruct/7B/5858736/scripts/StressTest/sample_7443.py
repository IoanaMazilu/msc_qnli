income_premise = 0.3
petrol_scooter_premise = 0.14
house_rent_premise = 0.14
food_premise = 0.52

income_hypothesis = 0.6
petrol_scooter_hypothesis = 0.14
house_rent_hypothesis = 0.14
food_hypothesis = 0.52

# the hypothesis refers to the percentage of income spent on petrol and scooter, referenced also in the premise
if petrol_scooter_hypothesis <= petrol_scooter_premise:
    # check if the estimate of 'petrol_scooter_hypothesis' contradicts the percentage of petrol spent in the premise
    label = "contradiction"
elif house_rent_hypothesis!= house_rent_premise:
    # check if the percentage of income spent on house rent in the hypothesis contradicts the percentage of house rent spent in the premise
    label = "contradiction"
elif food_hypothesis!= food_premise:
    # check if the percentage of income spent on food in the hypothesis contradicts the percentage of food spent in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
