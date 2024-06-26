deceased_premise = 12
deceased_hypothesis = 12
victims_premise = 5
victims_hypothesis = 5

# the hypothesis mentions the number of deceased and victims, which are also mentioned in the premise
if victims_hypothesis!= victims_premise:
    # check if the number of victims in the hypothesis contradicts the number of victims in the premise
    label = "contradiction"
elif deceased_hypothesis!= deceased_premise:
    # check if the number of deceased in the hypothesis contradicts the number of deceased in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
