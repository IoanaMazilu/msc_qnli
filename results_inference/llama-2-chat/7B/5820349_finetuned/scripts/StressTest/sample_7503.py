stretch_time_premise = 10
stretch_time_hypothesis = 20

# the hypothesis refers to the time when Pat stops to stretch, which is also mentioned in the premise
if stretch_time_premise >= stretch_time_hypothesis:
    # check if the time'stretch_time_premise' contradicts the estimate of less than'stretch_time_hypothesis'
    label = "contradiction"
elif stretch_time_premise < stretch_time_hypothesis:
    # the premise gives an exact time when Pat stops to stretch
    # any time less than'stretch_time_hypothesis' is consistent with the hypothesis, but cannot be explicitly entailed from the hypothesis
    label = "entailment"

print(label)
