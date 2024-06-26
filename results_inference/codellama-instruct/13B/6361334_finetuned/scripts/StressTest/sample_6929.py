sandy_age_premise = 4
sandy_age_hypothesis = 5
molly_age_premise = 3
molly_age_hypothesis = 3

# the hypothesis refers to the ratio between the ages of Sandy and Molly, which is also mentioned in the premise
if sandy_age_hypothesis!= sandy_age_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif molly_age_hypothesis!= molly_age_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
