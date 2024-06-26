jogging_walking_time_premise = 3
jogging_walking_time_hypothesis = 6

# the hypothesis refers to the total time Aaron spends jogging and walking, mentioned also in the premise
if jogging_walking_time_premise != jogging_walking_time_hypothesis:
    # check if the total time in the hypothesis contradicts the total time stated in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
