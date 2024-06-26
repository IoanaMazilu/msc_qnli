sandy_age_premise = 4
molly_age_premise = 3
sandy_age_hypothesis = 4
molly_age_hypothesis = 3

# the hypothesis refers to the ratio between the ages of Sandy and Molly, mentioned in the premise
if sandy_age_hypothesis <= sandy_age_premise:
    # check if the estimate of'sandy_age_hypothesis' contradicts the number of cookie sales in the premise
    label = "contradiction"
elif molly_age_hypothesis!= molly_age_premise:
    # check if the number of sold pies in the hypothesis contradicts the number of sold pies reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
