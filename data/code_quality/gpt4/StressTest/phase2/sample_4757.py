knitting_time_premise = 6
knitting_time_hypothesis = 6

# the hypothesis refers to the time Sita takes to knit, also mentioned in the premise
if knitting_time_hypothesis < knitting_time_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif knitting_time_hypothesis == knitting_time_premise:
    # check if the hypothesis value is exactly equal to the premise value
    label = "entailment"
else:
    # the hypothesis suggests that Sita takes more than 'knitting_time_hypothesis' days
    # this does not contradict the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
