# Define variables for the numerical entities in the premise and hypothesis
john_time_premise = 30
todd_time_premise = 60
john_time_hypothesis = float(input("Enter the time it takes John to rake the lawn (in minutes): "))
todd_time_hypothesis = 60

# Check if the hypothesis values contradict the premise values
if john_time_hypothesis > todd_time_premise:
    label = "contradiction"
elif john_time_hypothesis < todd_time_premise:
    label = "entailment"
else:
    # If the hypothesis values are equal to the premise values, there is no contradiction or entailment
    label = "neutral"

print(label)
