# Premise: Evan ran a mile in 10 minutes Monday morning, and he ran the same mile in 8 minutes on Tuesday morning.
# Hypothesis: Evan ran a mile in less than 10 minutes Monday morning, and he ran the same mile in 8 minutes on Tuesday morning.
# Golden Label: contradiction

monday_run_time_premise = 10
monday_run_time_hypothesis = 10
tuesday_run_time_premise = 8
tuesday_run_time_hypothesis = 8

# the hypothesis refers to the time Evan took to run a mile on Monday and Tuesday mornings mentioned in the premise
if monday_run_time_hypothesis < monday_run_time_premise:
    # check if the estimate of 'monday_run_time_hypothesis' contradicts the time reported for Monday run in the premise
    label = "contradiction"
elif tuesday_run_time_hypothesis != tuesday_run_time_premise:
    # check if the time for Tuesday run in the hypothesis contradicts the time reported for Tuesday run in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

