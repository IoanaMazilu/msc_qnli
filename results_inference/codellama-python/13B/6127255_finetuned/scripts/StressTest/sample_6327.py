cigarettes_per_minute_premise = 10
cigarettes_per_minute_hypothesis = 20

# the hypothesis refers to the number of boxes of cigarettes Kramer can pack per minute, mentioned in the premise
if cigarettes_per_minute_premise >= cigarettes_per_minute_hypothesis:
    # check if the number of boxes of cigarettes Kramer can pack per minute in the premise contradicts the hypothesis
    label = "contradiction"
else:
    # if the premise value does not contradict the hypothesis, we can infer entailment
    label = "entailment"

print(label)
