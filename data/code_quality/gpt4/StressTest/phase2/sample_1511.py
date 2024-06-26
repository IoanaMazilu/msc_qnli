stretch_time_premise = 27
stretch_time_hypothesis = 87

# the hypothesis talks about the time it takes Cathy to stretch, which is also mentioned in the premise
if stretch_time_hypothesis != stretch_time_premise:
    # check if the stretch time in the hypothesis contradicts the stretch time mentioned in the premise
    label = "contradiction"
else:
    # if the stretch times do not contradict, we can infer entailment
    label = "entailment"

print(label)
