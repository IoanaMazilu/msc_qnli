john_future_age_relation_premise = 2
john_future_age_relation_hypothesis = 8

# the hypothesis refers to the relation of John's and Tom's future age mentioned in the premise
if john_future_age_relation_premise != john_future_age_relation_hypothesis:
    # check if the hypothesis relation contradicts the relation reported in the premise
    label = "contradiction"
else:
    # if the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
