sponseller_premise = "The Citadel"
sponseller_hypothesis = "South Carolina Hospitality Association"

# the hypothesis mentions the name of the organization that Tom Sponseller is the head of, which is also mentioned in the premise
if sponseller_hypothesis!= sponseller_premise:
    # check if the name of the organization in the hypothesis contradicts the name of the organization in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
