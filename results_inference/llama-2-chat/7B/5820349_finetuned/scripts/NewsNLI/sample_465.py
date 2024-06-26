min_fine_premise = 10000
max_fine_premise = 29000000
max_fine_hypothesis = 4500000

# the hypothesis mentions the maximum amount of outstanding fines, which is also referenced in the premise
if max_fine_hypothesis > max_fine_premise:
    # check if the maximum fine in the hypothesis contradicts the maximum fine reported in the premise
    label = "contradiction"
else:
    # if the maximum fine in the hypothesis does not contradict the maximum fine in the premise, we can infer entailment
    label = "entailment"

print(label)
