# Premise: A bee has 6.0 legs and the legs are split on 2.0 sides of their body.
# Hypothesis: 3.0 legs are on a side.
# Golden Label: entailment

legs_bee_premise = 6.0
sides_body_premise = 2.0
legs_side_hypothesis = 3.0

# the hypothesis refers to the number of legs on a side, which can be inferred from the premise
# compute the number of legs on a side in the premise
legs_side_premise = legs_bee_premise / sides_body_premise
if legs_side_hypothesis != legs_side_premise:
    # check if the number of legs on a side in the hypothesis contradicts the number of legs on a side from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

