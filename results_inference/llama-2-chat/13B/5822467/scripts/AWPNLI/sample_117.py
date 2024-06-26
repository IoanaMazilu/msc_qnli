jogged_distance_premise = 25.0
jogged_time_premise = 5.0
hypothesis_time = 4.0

# convert hypothesis time from hours to kilometers per hour
hypothesis_speed = hypothesis_time * 5.0  # assume 5 km/h is the speed of jogging

# compute the total distance jogged based on the hypothesis
total_distance_hypothesis = jogged_distance_premise * hypothesis_speed

if total_distance_hypothesis!= jogged_distance_premise:
    # check if the total distance in the hypothesis contradicts the distance in the premise
    label = "contradiction"
elif hypothesis_speed!= 5.0:
    # check if the speed in the hypothesis contradicts the speed in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
