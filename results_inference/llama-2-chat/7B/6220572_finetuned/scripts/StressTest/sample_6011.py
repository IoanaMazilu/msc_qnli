race_distance_premise = 4
race_distance_hypothesis = 6
race_time_start_premise = 4
race_time_start_hypothesis = 4

# the hypothesis refers to the race distance and time start mentioned in the premise
if race_distance_hypothesis == race_distance_premise and race_time_start_hypothesis == race_time_start_premise:
    # check if the hypothesis values and estimates contradict the premise ones
    label = "entailment"
elif race_distance_hypothesis!= race_distance_premise or race_time_start_hypothesis!= race_time_start_premise:
    # check if the number of sold pies in the hypothesis contradicts the number of sold pies reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "neutral"

print(label)
