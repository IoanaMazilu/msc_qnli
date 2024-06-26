distance_premise = 50
walking_speed_premise = 4
running_speed_premise = 6

# the hypothesis talks about the distance traveled by Brad, referenced also in the premise
if distance_hypothesis > distance_premise:
    # check if the hypothesis value contradicts the estimate of less than 'distance_premise'
    label = "contradiction"
elif walking_speed_hypothesis!= walking_speed_premise or running_speed_hypothesis!= running_speed_premise:
    # check if the speed of Maxwell or Brad contradicts the speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
