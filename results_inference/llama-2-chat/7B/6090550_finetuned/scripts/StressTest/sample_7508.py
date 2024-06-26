stretch_time_premise = 20
stretch_time_hypothesis = 80

# the hypothesis refers to the time Pat takes to stretch, which is also mentioned in the premise
if stretch_time_hypothesis!= stretch_time_premise:
    # check if the stretch time in the hypothesis contradicts the stretch time in the premise
    label = "contradiction"
else:
    # if the stretch time in the hypothesis matches the one in the premise, we can infer entailment
    label = "entailment"

print(label)
