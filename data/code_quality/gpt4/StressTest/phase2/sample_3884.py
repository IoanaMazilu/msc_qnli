total_time_premise = 3
total_time_hypothesis = 3

# the hypothesis refers to the total time spent by Aaron jogging and walking mentioned in the premise
if total_time_hypothesis > total_time_premise:
    # check if the 'total_time_hypothesis' contradicts the total time in the premise
    label = "contradiction"
elif total_time_hypothesis < total_time_premise:
    # check if the total time in the hypothesis is less than the total time reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
