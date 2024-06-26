# Define variables for the premise and hypothesis
premise_distance = 7
premise_time = 1.25
hypothesis_distance = 3
hypothesis_time = 1.25

# Calculate the rates of walking for the premise and hypothesis
premise_rate = premise_distance / premise_time
hypothesis_rate = hypothesis_distance / hypothesis_time

# Compare the rates of walking for the premise and hypothesis
if premise_rate == hypothesis_rate:
    label = "entailment"
elif premise_rate > hypothesis_rate:
    label = "contradiction"
else:
    label = "neutral"

print(label)
