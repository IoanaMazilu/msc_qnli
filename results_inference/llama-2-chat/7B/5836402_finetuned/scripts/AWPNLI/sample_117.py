kilometers_premise = 25.0
kilometers_per_hour_premise = 5.0
hours_hypothesis = 4.0

# the hypothesis refers to the time Teresa jogged, which can be computed from the premise
# compute the time Teresa jogged in the premise
time_jogged_premise = kilometers_premise / kilometers_per_hour_premise
if hours_hypothesis!= time_jogged_premise:
    # check if the time from the hypothesis contradicts the time from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
