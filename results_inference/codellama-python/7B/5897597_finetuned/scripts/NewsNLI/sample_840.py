ipads_premise = 2
ipads_hypothesis = 2

# the hypothesis mentions the number of iPads planted, which is also referenced in the premise
if ipads_hypothesis!= ipads_premise:
    # check if the number of iPads in the hypothesis contradicts the number of iPads reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
