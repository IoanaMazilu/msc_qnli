ipads_found_premise = 2
ipads_planted_hypothesis = 2

# the hypothesis mentions the number of iPads planted, which is also referenced in the premise
if ipads_found_premise!= ipads_planted_hypothesis:
    # check if the number of iPads found contradicts the number of iPads planted in the hypothesis
    label = "contradiction"
else:
    # if the number of iPads found does not contradict the number of iPads planted in the hypothesis, we can infer entailment
    label = "entailment"

print(label)
