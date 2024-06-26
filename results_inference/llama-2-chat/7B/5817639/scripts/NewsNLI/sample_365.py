claims_premise = 4
claims_hypothesis = 4

# the hypothesis mentions the same entity (Agnieszka Radwanska) as the premise
if claims_hypothesis == claims_premise:
    # if the hypothesis and premise refer to the same entity, we can infer entailment
    label = "entailment"
else:
    # if the hypothesis and premise refer to different entities, we can check for contradiction
    label = "contradiction"

print(label)
