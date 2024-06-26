# Define variables with representative names for the numerical entities in both inputs
ministry_statement = "Experts determined that the two explosive devices were planted in one of the trees in the area, the ministry said, adding that an investigation was under way."
hypothesis = "It says that two explosive devices were in trees in the area."

# Extract all quantities as valid numbers (integers or floats)
ministry_statement_explosive_devices = 2
ministry_statement_trees = 1
ministry_statement_investigation = "under way"
hypothesis_explosive_devices = 2
hypothesis_trees = 1

# Use brief comments to explain what comparison you do between the defined variables
# Do not use their values in the comments
if ministry_statement_explosive_devices!= hypothesis_explosive_devices:
    # Check if the number of explosive devices mentioned in the ministry statement contradicts the number of explosive devices mentioned in the hypothesis
    label = "contradiction"
elif ministry_statement_trees!= hypothesis_trees:
    # Check if the number of trees mentioned in the ministry statement contradicts the number of trees mentioned in the hypothesis
    label = "contradiction"
elif ministry_statement_investigation!= "under way":
    # Check if the investigation mentioned in the ministry statement contradicts the information that an investigation is under way in the hypothesis
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
