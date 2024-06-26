stretch_time_premise = 12
stretch_time_hypothesis = 42

# the hypothesis refers to the time when Cathy stops to stretch, mentioned in the premise
if stretch_time_premise >= stretch_time_hypothesis:
    # check if the premise 'stretch_time_premise' contradicts the upper limit for the stretch time in the hypothesis
    label = "contradiction"
elif stretch_time_premise < stretch_time_hypothesis:
    # check if the premise 'stretch_time_premise' is less than the upper limit for the stretch time in the hypothesis
    label = "entailment"
else:
    # if the hypothesis estimate does not contradict the premise and is not less than the premise, we infer neutral
    label = "neutral"

print(label)
