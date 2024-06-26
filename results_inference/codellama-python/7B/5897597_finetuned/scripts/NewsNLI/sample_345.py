deceased_premise = 12
deceased_hypothesis = 12
physically_paralyzed_premise = 5
physically_paralyzed_hypothesis = 5

# the hypothesis mentions the number of deceased and physically paralyzed people, which are also mentioned in the premise
if deceased_hypothesis!= deceased_premise:
    # check if the number of deceased people in the hypothesis contradicts the number of deceased people reported in the premise
    label = "contradiction"
elif physically_paralyzed_hypothesis!= physically_paralyzed_premise:
    # check if the number of physically paralyzed people from the hypothesis contradicts the number of physically paralyzed people in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
