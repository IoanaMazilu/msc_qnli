stretch_time_premise = 10
stretch_time_hypothesis = 60

# the hypothesis refers to the time when Pat stops to stretch, mentioned in the premise
if stretch_time_hypothesis!= stretch_time_premise:
    # check if the time in the hypothesis contradicts the time reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
