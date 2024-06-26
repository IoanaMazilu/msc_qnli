labels = ["entailment", "contradiction", "neutral"]

premise = "Earlier, South American champions Internacional took third place with a 4-2 win over Seongnam Ilhwa Chunma of South Korea with Alecsandro scoring twice."
hypothesis = "Internacional of Brazil beat Seongnam Ilhwa Chunma 4-2 in third place playoff."

# Define variables for the premise and hypothesis
premise_labels = ["Internacional", "Seongnam Ilhwa Chunma", "Alecsandro"]
hypothesis_labels = ["Internacional", "Seongnam Ilhwa Chunma"]

# Extract quantities from the premise and hypothesis
premise_quantities = {
    "Internacional": 1,
    "Seongnam Ilhwa Chunma": 1,
    "Alecsandro": 2
}
hypothesis_quantities = {
    "Internacional": 1,
    "Seongnam Ilhwa Chunma": 1
}

# Check for contradictions
for label in premise_labels:
    if premise_quantities[label]!= hypothesis_quantities[label]:
        label = "contradiction"
        break
else:
    label = "entailment"

print(label)
