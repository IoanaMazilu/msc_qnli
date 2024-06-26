stretch_time_premise = 10
stretch_time_hypothesis = 20

# the hypothesis refers to the time when Pat stops to stretch, which is also mentioned in the premise
if stretch_time_premise >= stretch_time_hypothesis:
    # check if the time in the premise contradicts the estimate of less than'stretch_time_hypothesis'
    label = "contradiction"
else:
    # if the premise time does not contradict the hypothesis time, we can infer entailment
    label = "entailment"

print(label)
