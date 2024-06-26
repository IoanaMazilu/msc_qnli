# Define variables with representative names for the numerical entities in both inputs
men_employed_premise = 100
km_highway_premise = 2
days_working_premise = 50
hours_per_day_premise = 8

men_employed_hypothesis = 600

# Extract all quantities as valid numbers
men_employed_premise = int(men_employed_premise)
km_highway_premise = int(km_highway_premise)
days_working_premise = int(days_working_premise)
hours_per_day_premise = int(hours_per_day_premise)
men_employed_hypothesis = int(men_employed_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
if men_employed_hypothesis <= men_employed_premise:
    # Check if the estimate of'men_employed_hypothesis' contradicts the number of men employed in the premise
    label = "contradiction"
elif km_highway_premise!= km_highway_hypothesis:
    # Check if the number of km in the hypothesis contradicts the number of km reported in the premise
    label = "contradiction"
elif days_working_premise!= days_working_hypothesis:
    # Check if the number of days working in the hypothesis contradicts the number of days working reported in the premise
    label = "contradiction"
elif hours_per_day_premise!= hours_per_day_hypothesis:
    # Check if the number of hours per day working in the hypothesis contradicts the number of hours per day working reported in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
