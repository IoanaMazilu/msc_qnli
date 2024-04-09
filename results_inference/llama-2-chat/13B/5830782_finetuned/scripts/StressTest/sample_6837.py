earnings_premise = 9000
earnings_hypothesis = 4000

# the hypothesis refers to the total earnings of 'he' and 'Rick' mentioned in the premise
if earnings_premise <= earnings_hypothesis:
    # check if the estimate of 'earnings_hypothesis' contradicts the total earnings in the premise
    label = "contradiction"
else:
    # if the hypothesis estimate does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
