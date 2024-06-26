ntc_injuries_premise = 30
ntc_injuries_hypothesis = 30

# the hypothesis mentions the number of NTC fighters' injuries, which is also referenced in the premise
if ntc_injuries_hypothesis != ntc_injuries_premise:
    # check if the number of injuries in the hypothesis contradicts the number of injuries reported in the premise
    label = "contradiction"
else:
    # if the number of injuries in the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
