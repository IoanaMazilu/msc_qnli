match_points_saved_premise = 3
match_points_saved_hypothesis = 3

# the hypothesis mentions the number of match points saved by Soderling, which is also referenced in the premise
# the hypothesis does not provide any additional numerical information that contradicts the premise
if match_points_saved_hypothesis != match_points_saved_premise:
    # check if the number of match points saved in the hypothesis contradicts the number of match points saved in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
