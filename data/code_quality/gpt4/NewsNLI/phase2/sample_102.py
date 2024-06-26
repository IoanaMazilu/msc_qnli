shots_adrift_premise = 14
shots_adrift_hypothesis = 14

# the hypothesis mentions the number of shots that Stacy Lewis finished behind Park, which is also mentioned in the premise

if shots_adrift_hypothesis != shots_adrift_premise:
    # check if the number of shots from the hypothesis contradicts the number of shots in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
