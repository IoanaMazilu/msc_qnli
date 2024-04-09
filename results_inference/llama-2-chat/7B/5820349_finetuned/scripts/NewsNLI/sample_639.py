favorable_view_premise = 0.15
favorable_view_hypothesis = 0.10

# the hypothesis mentions the percentage of Saudis who have a favorable view of al Qaeda, which is also referenced in the premise
if favorable_view_hypothesis!= favorable_view_premise:
    # check if the percentage in the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
else:
    # if the percentage in the hypothesis does not contradict the percentage in the premise, we can infer entailment
    label = "entailment"

print(label)
