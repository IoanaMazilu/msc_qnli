# Define variables for the premise and hypothesis
premise_distance = 7
premise_time = 1.25
hypothesis_distance = 2
hypothesis_time = 1.25

# Calculate the rate of walking for the premise
premise_rate = premise_distance / premise_time

# Calculate the rate of walking for the hypothesis
hypothesis_rate = hypothesis_distance / hypothesis_time

# Check if the hypothesis rate is greater than the premise rate
if hypothesis_rate > premise_rate:
    label = "entailment"
else:
    label = "contradiction"

print(label)
