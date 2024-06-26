saved_premise = 10
discount_premise = 15

saved_hypothesis = 10
discount_hypothesis = 15

# the premise and hypothesis are talking about the savings and discount on a sweater
if saved_hypothesis != saved_premise:
    # check if the savings mentioned in the hypothesis contradict the savings mentioned in the premise
    label = "contradiction"
elif discount_premise != discount_hypothesis:
    # check if the discount mentioned in the hypothesis contradicts the discount mentioned in the premise
    label = "contradiction"
else:
    # if all the mentioned values and conditions in the hypothesis match exactly with the premise, we can infer entailment
    label = "entailment"

print(label)
