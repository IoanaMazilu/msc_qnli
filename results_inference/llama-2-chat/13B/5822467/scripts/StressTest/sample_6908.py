# Define variables for numerical entities in the premise and hypothesis
hrs_at_44_premise = 1
hrs_at_60_premise = 3
mph_at_44_premise = 44
mph_at_60_premise = 60

# Define variables for numerical entities in the hypothesis
hrs_at_44_hypothesis = less_than_1
hrs_at_60_hypothesis = 3
mph_at_44_hypothesis = 44
mph_at_60_hypothesis = 60

# Perform calculations and comparisons as needed
if hrs_at_44_hypothesis <= hrs_at_44_premise and hrs_at_60_hypothesis <= hrs_at_60_premise:
    # Check if the hypothesis values and estimates do not contradict the premise ones
    label = "entailment"
elif mph_at_44_hypothesis > mph_at_44_premise or mph_at_60_hypothesis > mph_at_60_premise:
    # Check if the hypothesis values contradict the premise values
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "neutral"

print(label)
