premise_distance = 25.0
premise_speed = 5.0
hypothesis_time = 4.0

# the hypothesis refers to the time, which is also mentioned in the premise
# compute the total distance jogged in the premise
total_distance_premise = premise_distance / premise_speed
if hypothesis_time >= total_distance_premise:
    # check if the time from the hypothesis is greater than or equal to the total distance jogged in the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer contradiction
    label = "contradiction"

print(label)
