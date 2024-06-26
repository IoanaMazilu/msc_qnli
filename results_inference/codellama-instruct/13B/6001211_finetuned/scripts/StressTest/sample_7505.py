stretch_time_premise = 10
stretch_time_hypothesis = 60

# the hypothesis refers to the time when Pat stops to stretch, mentioned in the premise
if stretch_time_hypothesis == stretch_time_premise:
    # check if the hypothesis time contradicts the premise time
    label = "entailment"
elif stretch_time_hypothesis!= stretch_time_premise:
    # check if the hypothesis time contradicts the premise time
    label = "contradiction"
else:
    # if the hypothesis time does not contradict the premise time, we can infer neutrality
    label = "neutral"

print(label)
