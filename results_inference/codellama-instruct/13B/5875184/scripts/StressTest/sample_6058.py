premise_days = [38, 27, 36]
hypothesis_days = [18, 27, 36]

# check if the hypothesis values contradict the premise estimates
if any(hypothesis_days[i] < premise_days[i] for i in range(len(premise_days))):
    label = "contradiction"
elif all(hypothesis_days[i] <= premise_days[i] for i in range(len(premise_days))):
    label = "entailment"
else:
    label = "neutral"

print(label)
