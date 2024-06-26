average_victims_per_day_premise = 8000
days_premise = 100
total_victims_hypothesis = 800000

# Calculate total victims based on the average victims per day and number of days in the premise
total_victims_premise = average_victims_per_day_premise * days_premise

# Check if the total victims in the hypothesis matches with the calculated total victims in the premise
if total_victims_premise == total_victims_hypothesis:
    label = "entailment"
else:
    label = "contradiction"

print(label)
