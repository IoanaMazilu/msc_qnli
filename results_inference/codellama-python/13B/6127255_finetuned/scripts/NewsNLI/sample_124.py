injuries_premise = 30
injuries_hypothesis = 30

# the hypothesis mentions the number of injuries in the NTC fighters, which is also mentioned in the premise
if injuries_hypothesis!= injuries_premise:
    # check if the number of injuries in the hypothesis contradicts the number of injuries reported in the premise
    label = "contradiction"
else:
    # if the number of injuries in the hypothesis does not contradict the number of injuries in the premise, we can infer entailment
    label = "entailment"

print(label)
