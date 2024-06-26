# Define variables for the premise and hypothesis
premise_rate = 1st_quarter
hypothesis_rate = 25

# Check if the number of years mentioned in the hypothesis contradicts the premise
if hypothesis_rate > premise_rate:
    label = "contradiction"
elif hypothesis_rate < premise_rate:
    label = "entailment"
else:
    label = "neutral"

print(label)
