stretch_time_premise = 30
stretch_time_hypothesis = 80

# the hypothesis talks about the time when Jim stops to stretch, referenced also in the premise
if stretch_time_hypothesis!= stretch_time_premise:
    # check if the time when Jim stops to stretch in the hypothesis contradicts the time mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis time does not contradict the premise time, we can infer entailment
    label = "entailment"

print(label)
