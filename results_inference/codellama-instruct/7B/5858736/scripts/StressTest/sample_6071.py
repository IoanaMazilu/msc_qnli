# Define variables for the numerical entities in the premise and hypothesis
premise_builder_number = 2
premise_building_days = 15
premise_homes_number = 100

hypothesis_builder_number = 2
hypothesis_building_days = 15
hypothesis_homes_number = 100

# Extract all quantities as valid numbers
premise_builder_number = int(premise_builder_number)
premise_building_days = int(premise_building_days)
premise_homes_number = int(premise_homes_number)

hypothesis_builder_number = int(hypothesis_builder_number)
hypothesis_building_days = int(hypothesis_building_days)
hypothesis_homes_number = int(hypothesis_homes_number)

# Check if the hypothesis values and estimates do not contradict the premise ones
if hypothesis_builder_number!= premise_builder_number:
    label = "contradiction"
elif hypothesis_building_days!= premise_building_days:
    label = "contradiction"
elif hypothesis_homes_number!= premise_homes_number:
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
