# Premise: After 40 minutes, Annie stops to fix a flat tire.
# Hypothesis: After more than 40 minutes, Annie stops to fix a flat tire.
# Golden Label: contradiction

time_premise = 40
time_hypothesis = 40

# the hypothesis mentions the time after which Annie stops to fix a flat tire, which is also referred to in the premise
if time_hypothesis < time_premise:
    # check if the hypothesis value contradicts the exact time 'time_premise' mentioned in the premise
    label = "contradiction"
elif time_hypothesis > time_premise:
    # the premise gives the exact time when Annie stops
    # any time more than 'time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)

