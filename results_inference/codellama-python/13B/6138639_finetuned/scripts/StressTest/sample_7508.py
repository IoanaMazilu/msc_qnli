stretch_time_premise = 20
stretch_time_hypothesis = 80

# the hypothesis talks about the time Pat takes to stretch, referenced also in the premise
if stretch_time_hypothesis!= stretch_time_premise:
    # check if the time Pat takes to stretch in the hypothesis contradicts the time Pat takes to stretch in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
