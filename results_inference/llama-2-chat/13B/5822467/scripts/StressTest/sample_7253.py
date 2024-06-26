suraj_avg_premise = 8
suraj_avg_hypothesis = 4

# the hypothesis refers to the number of innings played by Suraj
if suraj_avg_hypothesis <= suraj_avg_premise:
    # check if the hypothesis value contradicts the estimate of'suraj_avg_premise'
    label = "contradiction"
elif suraj_avg_hypothesis!= suraj_avg_premise:
    # check if the number of innings played in the hypothesis contradicts the number of innings reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
