jogging_premise = 4
jogging_hypothesis = 3
walking_premise = 1

# the hypothesis refers to the total time spent jogging and walking
if jogging_hypothesis + walking_premise <= jogging_premise:
    # check if the hypothesis value contradicts the estimate of less than 'jogging_premise'
    label = "contradiction"
elif jogging_hypothesis!= jogging_premise:
    # check if the number of miles jogged in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
