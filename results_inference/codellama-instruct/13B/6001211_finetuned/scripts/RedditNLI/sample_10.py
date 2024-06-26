rupee_rate_premise = 65.36
rupee_rate_hypothesis = 68.19
sensex_points_fall_premise = 300
sensex_points_fall_hypothesis = 282.50
sensex_index_premise = 17685.58
sensex_index_hypothesis = 17685.58

# the hypothesis and premise mention the rupee rate, sensex points fall and sensex index
if rupee_rate_hypothesis < rupee_rate_premise:
    # check if the rupee rate in the hypothesis contradicts the premise
    label = "contradiction"
elif sensex_points_fall_hypothesis!= sensex_points_fall_premise:
    # check if the sensex points fall in the hypothesis contradicts the premise
    label = "contradiction"
elif sensex_index_hypothesis!= sensex_index_premise:
    # check if the sensex index in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
