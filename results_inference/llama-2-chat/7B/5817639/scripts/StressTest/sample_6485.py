distance_premise = 20
distance_hypothesis = 20
walking_speed_premise = 4
walking_speed_hypothesis = 4
running_speed_premise = 6
running_speed_hypothesis = 6

# the hypothesis refers to the distance traveled by Brad, which is also mentioned in the premise
if distance_hypothesis <= distance_premise:
    # check if the estimate of 'distance_hypothesis' contradicts the distance traveled in the premise
    label = "contradiction"
elif walking_speed_hypothesis!= walking_speed_premise or running_speed_hypothesis!= running_speed_premise:
    # check if the speed of Brad in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
