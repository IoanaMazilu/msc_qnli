favorable_view_premise = 0.15
favorable_view_hypothesis = 0.10

# the hypothesis mentions the percentage of Saudis with a favorable view of al Qaeda, which is also mentioned in the premise
if favorable_view_hypothesis!= favorable_view_premise:
    # check if the percentage of favorable view in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
