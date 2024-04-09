# Variables for premise and hypothesis
premise_rate = 65.36
hypothesis_rate = 68.19

# Check for contradictions
if hypothesis_rate < premise_rate:
    label = "contradiction"
elif hypothesis_rate > premise_rate:
    label = "entailment"
else:
    label = "neutral"

print(label)
