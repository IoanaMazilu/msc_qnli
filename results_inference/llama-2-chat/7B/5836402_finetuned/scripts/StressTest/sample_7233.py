# defining the variables for the premise and hypothesis
running_distance_premise = 2
running_distance_hypothesis = 3

# the hypothesis refers to the distance run by the twin sisters mentioned in the premise
if running_distance_premise >= running_distance_hypothesis:
    # check if the estimate of 'running_distance_hypothesis' contradicts the distance run in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
