# Define variables with representative names for the numerical entities in both inputs
bottom_half_population_premise = 85
richest_people_premise = 85
half_world_population_hypothesis = 50

# Extract all quantities as valid numbers (integers or floats)
bottom_half_population_premise = int(bottom_half_population_premise)
richest_people_premise = int(richest_people_premise)
half_world_population_hypothesis = int(half_world_population_hypothesis)

# Perform calculations if necessary
# In this case, we don't need to perform any calculations

# Compare the variables
if bottom_half_population_premise!= half_world_population_hypothesis:
    # Check if the number of people in the hypothesis contradicts the number of people in the premise
    label = "contradiction"
elif richest_people_premise == half_world_population_hypothesis:
    # Check if the estimated percentage of the population in the hypothesis is consistent with the premise estimate of 85 richest people owning as much as the bottom half of the population
    label = "entailment"
else:
    # The premise gives only an estimate for the percentage of the population
    # Any estimate of the percentage in the hypothesis greater or equal to the premise estimate is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
