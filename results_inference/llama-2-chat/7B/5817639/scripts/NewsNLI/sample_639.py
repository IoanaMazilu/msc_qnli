view_premise = 0.15
view_hypothesis = 0.10

# the hypothesis mentions the percentage of Saudis with a favorable view of al Qaeda, which is also referenced in the premise
if view_hypothesis!= view_premise:
    # check if the percentage of Saudis with a favorable view of al Qaeda in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
