stretch_time_premise = 20
stretch_time_hypothesis = 80

# the hypothesis refers to the time it takes Pat to stretch, also mentioned in the premise
if stretch_time_hypothesis!= stretch_time_premise:
    # check if the stretch time in the hypothesis contradicts the stretch time mentioned in the premise
    label = "contradiction"
else:
    # if the stretch time in the hypothesis does not contradict the stretch time in the premise, we can infer entailment
    label = "entailment"

print(label)
