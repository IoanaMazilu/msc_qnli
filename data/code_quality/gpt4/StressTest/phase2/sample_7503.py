stretch_time_premise = 10
stretch_time_hypothesis = 20

# the hypothesis refers to the time when Pat stops to stretch mentioned in the premise
if stretch_time_premise >= stretch_time_hypothesis:
    # check if 'stretch_time_premise' contradicts the hypothesis that Pat stops to stretch in less than 'stretch_time_hypothesis' minutes
    label = "contradiction"
elif stretch_time_premise == stretch_time_hypothesis-10:
    # if 'stretch_time_premise' is exactly 10 minutes less than 'stretch_time_hypothesis', we can infer entailment
    label = "entailment"
else:
    # if 'stretch_time_premise' is less than 'stretch_time_hypothesis' but not exactly 10 minutes less, we can infer neutrality
    label = "neutral"

print(label)
