# Define variables for the number of gangs Mala has
num_gangs_premise = 5
num_gangs_hypothesis = 6

# Check if the hypothesis value contradicts the premise
if num_gangs_hypothesis <= num_gangs_premise:
    label = "contradiction"
else:
    # The hypothesis value is greater than the premise, so it cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
