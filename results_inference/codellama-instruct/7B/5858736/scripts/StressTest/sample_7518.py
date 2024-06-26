# Define variables with representative names for the numerical entities in both inputs
total_population_premise = 0
total_population_hypothesis = 0
boys_population_premise = 0
boys_population_hypothesis = 0

# Extract all quantities as valid numbers (integers or floats)
total_population_premise = float(input("Enter the total population of Jones Elementary: "))
total_population_hypothesis = float(input("Enter the total population of Jones Elementary: "))
boys_population_premise = float(input("Enter the number of boys in Jones Elementary: "))
boys_population_hypothesis = float(input("Enter the number of boys in Jones Elementary: "))

# Use brief comments to explain what comparison you do between the defined variables
if boys_population_premise / total_population_premise <= boys_population_hypothesis / total_population_hypothesis:
    # Check if the estimate of 'boys_population_hypothesis' contradicts the number of boys in the premise
    label = "contradiction"
elif total_population_hypothesis <= total_population_premise:
    # Check if the estimate of 'total_population_hypothesis' contradicts the total population in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
