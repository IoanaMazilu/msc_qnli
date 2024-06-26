stretch_time_premise = 18
stretch_time_hypothesis = 78

# the hypothesis refers to the time Jim takes to stretch, which is also mentioned in the premise
if stretch_time_hypothesis < stretch_time_premise:
    # check if the hypothesis time contradicts the premise time
    label = "contradiction"
elif stretch_time_hypothesis == stretch_time_premise:
    # check if the hypothesis time equals the premise time
    label = "neutral"
else:
    # if the hypothesis time is greater than the premise time, we can infer entailment
    label = "entailment"

print(label)
