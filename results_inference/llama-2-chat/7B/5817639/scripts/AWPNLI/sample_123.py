kilometers_premise = 4.0
kilometers_per_hour_premise = 3.0
time_premise = 2.9

# the hypothesis refers to the time spent walking, which is also mentioned in the premise
# compute the total distance walked in the premise
total_distance_premise = kilometers_premise * time_premise

# compare the distance walked in the hypothesis to the distance walked in the premise
if total_distance_hypothesis!= total_distance_premise:
    # check if the distance walked in the hypothesis contradicts the distance walked in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
