speed_premise = 7
speed_hypothesis = 2
meet_distance_premise = 0
meet_distance_hypothesis = 0

# the hypothesis talks about the speed of Fred and Sam
if speed_hypothesis <= speed_premise:
    # check if the hypothesis value contradicts the estimate of less than'speed_premise'
    label = "contradiction"
elif meet_distance_hypothesis!= meet_distance_premise:
    # check if the number of miles Sam walked in the hypothesis contradicts the number of miles Sam walked reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
