stretch_time_premise = 78
stretch_time_hypothesis = 18

# the hypothesis talks about the time Jim takes to stretch, which is also mentioned in the premise
if stretch_time_hypothesis >= stretch_time_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
