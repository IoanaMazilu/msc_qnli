total_time_premise = 3
total_time_hypothesis = 4

# the hypothesis talks about the total time spent jogging and walking, referenced also in the premise
if total_time_hypothesis!= total_time_premise:
    # check if the total time in the hypothesis contradicts the total time reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
