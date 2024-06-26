parts_made_in_usa_premise = 0.80
parts_made_in_usa_hypothesis = 0.80

# the hypothesis mentions the percentage of parts made in the U.S. on foreign vehicles, which is also referenced in the premise
# however, the hypothesis refers to a general condition (more than 80%) while the premise specifies a specific condition (80%)
if parts_made_in_usa_hypothesis <= parts_made_in_usa_premise:
    # check if the percentage of parts made in the U.S. in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
else:
    # if the hypothesis percentage does not contradict the premise percentage, we can infer entailment
    label = "entailment"

print(label)
