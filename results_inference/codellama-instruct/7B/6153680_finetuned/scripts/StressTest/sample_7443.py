petrol_spent_premise = 30
petrol_spent_hypothesis = 60
rent_spent_premise = 14
rent_spent_hypothesis = 14

# the hypothesis refers to the percentage of income spent on petrol and rent, which are also mentioned in the premise
if petrol_spent_hypothesis <= petrol_spent_premise:
    # check if the percentage of petrol spent in the hypothesis contradicts the percentage of petrol spent in the premise
    label = "contradiction"
elif rent_spent_hypothesis!= rent_spent_premise:
    # check if the percentage of rent spent in the hypothesis contradicts the percentage of rent spent in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
