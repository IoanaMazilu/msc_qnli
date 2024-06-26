share_difference_premise = 200
share_difference_hypothesis = 200

# the hypothesis refers to the difference in share between Mani and Rani, which is also mentioned in the premise
if share_difference_hypothesis!= share_difference_premise:
    # check if the difference in share in the hypothesis contradicts the difference in share reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
