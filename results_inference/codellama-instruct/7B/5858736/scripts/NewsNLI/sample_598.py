# Define variables for the numerical entities in the premise and hypothesis
premise_elevation = 1000
premise_landlocked = True
premise_country = "Lesotho"
premise_population = 2000000

hypothesis_landlocked = True
hypothesis_country = "Lesotho"
hypothesis_population = 2000000

# Extract all quantities as valid numbers
premise_elevation = float(premise_elevation)
hypothesis_elevation = float(hypothesis_elevation)
premise_population = int(premise_population)
hypothesis_population = int(hypothesis_population)

# Use brief comments to explain what comparison you do between the defined variables
if premise_elevation!= hypothesis_elevation:
    # check if the elevation in the hypothesis contradicts the elevation reported in the premise
    label = "contradiction"
elif premise_landlocked!= hypothesis_landlocked:
    # check if the landlocked status in the hypothesis contradicts the landlocked status in the premise
    label = "contradiction"
elif premise_country!= hypothesis_country:
    # check if the country name in the hypothesis contradicts the country name in the premise
    label = "contradiction"
elif premise_population!= hypothesis_population:
    # check if the population in the hypothesis contradicts the population in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
