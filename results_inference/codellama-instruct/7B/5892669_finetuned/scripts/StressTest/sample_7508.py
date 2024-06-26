stretch_time_premise = 20
stretch_time_hypothesis = 80

# the hypothesis refers to the time it takes Pat to stretch, which is also mentioned in the premise
if stretch_time_hypothesis!= stretch_time_premise:
    # check if the time in the hypothesis contradicts the time mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis time does not contradict the premise time, we can infer entailment
    label = "entailment"

print(label)