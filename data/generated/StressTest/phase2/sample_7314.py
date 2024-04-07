# Premise: After 30 minutes, Jim stops to stretch.
# Hypothesis: After less than 40 minutes, Jim stops to stretch.
# Golden Label: entailment

stretch_time_premise = 30
stretch_time_hypothesis = 40

# the hypothesis refers to the moment when Jim stops to stretch, which is also mentioned in the premise
if stretch_time_premise >= stretch_time_hypothesis:
    # check if the premise value contradicts the estimate of less than 'stretch_time_hypothesis'
    label = "contradiction"
elif stretch_time_premise != stretch_time_hypothesis:
    # the premise specifies exact time for Jim's stop
    # any time less than 'stretch_time_hypothesis' but not equal to 'stretch_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis value do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

