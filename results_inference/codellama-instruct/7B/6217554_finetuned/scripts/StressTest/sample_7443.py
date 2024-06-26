petrol_scooter_premise = 30
petrol_scooter_hypothesis = 60
rent_premise = 14
rent_hypothesis = 14

# the hypothesis refers to the percentage of income spent on petrol and rent, mentioned in the premise
if petrol_scooter_hypothesis <= petrol_scooter_premise:
    # check if the percentage of petrol spent in the hypothesis contradicts the percentage of petrol spent in the premise
    label = "contradiction"
elif rent_hypothesis!= rent_premise:
    # check if the percentage of rent spent in the hypothesis contradicts the percentage of rent spent in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
