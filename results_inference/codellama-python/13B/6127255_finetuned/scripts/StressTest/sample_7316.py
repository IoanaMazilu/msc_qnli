stretch_time_premise = 30
stretch_time_hypothesis = 80

# the hypothesis refers to the time when Jim stops to stretch, which is also mentioned in the premise
if stretch_time_hypothesis!= stretch_time_premise:
    # check if the hypothesis time contradicts the premise time
    label = "contradiction"
else:
    # if the hypothesis time does not contradict the premise time, we can infer entailment
    label = "entailment"

print(label)
