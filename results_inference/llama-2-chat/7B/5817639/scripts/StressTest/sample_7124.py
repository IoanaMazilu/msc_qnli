jogging_speed_premise = 4
jogging_speed_hypothesis = 3
walking_speed_premise = 8
walking_speed_hypothesis = 8

# the hypothesis refers to the speed of jogging and walking mentioned in the premise
if jogging_speed_premise <= jogging_speed_hypothesis:
    # check if the estimate of 'jogging_speed_hypothesis' contradicts the speed of jogging in the premise
    label = "contradiction"
elif walking_speed_hypothesis!= walking_speed_premise:
    # check if the speed of walking in the hypothesis contradicts the speed of walking reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
