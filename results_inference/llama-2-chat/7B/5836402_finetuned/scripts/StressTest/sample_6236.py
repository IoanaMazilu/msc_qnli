# Define variables for the premise and hypothesis
doubled_speed_premise = 2
doubled_speed_hypothesis = 2
house_cleaning_time_premise = 3
house_cleaning_time_hypothesis = 3

# The hypothesis refers to the same situation as the premise, but with a different time estimate
# Check if the hypothesis time estimate contradicts the premise time estimate
if doubled_speed_hypothesis <= doubled_speed_premise:
    label = "contradiction"
else:
    # If the hypothesis time estimate is greater than the premise time estimate, it is a new estimate
    # Therefore, we cannot infer entailment or contradiction based on this comparison
    label = "neutral"

print(label)
