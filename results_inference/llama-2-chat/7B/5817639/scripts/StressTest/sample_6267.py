% import sys

# Define variables for the numerical entities in the input sentences
premise_death_rate = float(sys.stdin.readline().rstrip())
remainder_left_premise = float(sys.stdin.readline().rstrip())
hypothesis_death_rate = float(sys.stdin.readline().rstrip())
remainder_left_hypothesis = float(sys.stdin.readline().rstrip())

# Extract all quantities as valid numbers
death_rate_premise = float(sys.stdin.readline().rstrip())
death_rate_hypothesis = float(sys.stdin.readline().rstrip())

# Compare the variables
if death_rate_hypothesis <= death_rate_premise:
    # Check if the hypothesis value contradicts the estimate of death rate in the premise
    label = "contradiction"
elif remainder_left_hypothesis!= remainder_left_premise:
    # Check if the number of people who left the village in the hypothesis contradicts the number of people who left the village in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
