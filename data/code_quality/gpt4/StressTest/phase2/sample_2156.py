stretch_time_pat_premise = 15
stretch_time_pat_hypothesis = 15

# the hypothesis refers to the time Pat spends stretching
if stretch_time_pat_hypothesis > stretch_time_pat_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
elif stretch_time_pat_hypothesis < stretch_time_pat_premise:
    # check if the premise value contradicts the hypothesis
    label = "contradiction"
else:
    # if the hypothesis value and premise value do not contradict each other, we can infer entailment
    label = "entailment"

print(label)
