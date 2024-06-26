# Define variables with representative names for the numerical entities in both inputs
agents_premise = 100
agents_hypothesis = 100
locations_premise = 70
locations_hypothesis = 70
provinces_premise = 10
provinces_hypothesis = 10
colombians_rescued_premise = 200
colombians_rescued_hypothesis = 200

# Extract all quantities as valid numbers (integers or floats)
agents_premise = int(agents_premise)
agents_hypothesis = int(agents_hypothesis)
locations_premise = int(locations_premise)
locations_hypothesis = int(locations_hypothesis)
provinces_premise = int(provinces_premise)
provinces_hypothesis = int(provinces_hypothesis)
colombians_rescued_premise = int(colombians_rescued_premise)
colombians_rescued_hypothesis = int(colombians_rescued_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
if agents_hypothesis!= agents_premise:
    # check if the number of agents in the hypothesis contradicts the number of agents in the premise
    label = "contradiction"
elif locations_hypothesis!= locations_premise:
    # check if the number of locations in the hypothesis contradicts the number of locations in the premise
    label = "contradiction"
elif provinces_hypothesis!= provinces_premise:
    # check if the number of provinces in the hypothesis contradicts the number of provinces in the premise
    label = "contradiction"
elif colombians_rescued_hypothesis!= colombians_rescued_premise:
    # check if the number of Colombians rescued in the hypothesis contradicts the number of Colombians rescued in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
