stretch_time_premise = 10
stretch_time_hypothesis = 60

# the hypothesis refers to the time when Pat stops to stretch, which is also mentioned in the premise
if stretch_time_hypothesis!= stretch_time_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
