premise_days = 5
hypothesis_days = 10

# the hypothesis refers to the duration of their work together
if hypothesis_days > premise_days:
    # the hypothesis explicitly entails the premise
    label = "entailment"
elif hypothesis_days == premise_days:
    # the hypothesis is consistent with the premise, but cannot be explicitly entailed
    label = "neutral"
else:
    # the hypothesis contradicts the premise
    label = "contradiction"

print(label)
