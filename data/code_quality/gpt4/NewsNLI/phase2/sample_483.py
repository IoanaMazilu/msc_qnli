participants_premise = 6000
participants_hypothesis = 6000

# the hypothesis mentions the number of participants in the study, which is also mentioned in the premise
if participants_hypothesis != participants_premise:
    # check if the number of participants in the hypothesis contradicts the number of participants in the premise
    label = "contradiction"
else:
    # if the number in the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
