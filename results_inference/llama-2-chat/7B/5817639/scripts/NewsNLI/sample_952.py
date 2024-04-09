# Variables for premise and hypothesis
premise_text = "'' He came in and already knows how to beat me in this game,'' 50 Cent said."
hypothesis_text = "Hip-hop artist 50 Cent lends his image and ideas to new video game."

# Extract numerical entities and their values
premise_numerical_entities = ["50 Cent", "game"]
hypothesis_numerical_entities = ["50 Cent", "video game"]

# Define variables for each numerical entity
premise_variables = {
    "50 Cent": 50,
    "game": 1
}
hypothesis_variables = {
    "50 Cent": 50,
    "video game": 1
}

# Check for contradictions
if premise_variables["50 Cent"]!= hypothesis_variables["50 Cent"]:
    label = "contradiction"
elif premise_variables["game"]!= hypothesis_variables["video game"]:
    label = "contradiction"
else:
    label = "entailment"

print(label)
