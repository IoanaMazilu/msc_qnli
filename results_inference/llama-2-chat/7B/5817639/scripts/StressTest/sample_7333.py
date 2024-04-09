% import sys

# Define variables for the premise and hypothesis
premise_percentage_users = float(sys.stdin.readline().strip())
hypothesis_percentage_users = float(sys.stdin.readline().strip())

# Check if the hypothesis value contradicts the premise value
if hypothesis_percentage_users > premise_percentage_users:
    label = "contradiction"
elif hypothesis_percentage_users < premise_percentage_users:
    label = "entailment"
else:
    label = "neutral"

print(label)
