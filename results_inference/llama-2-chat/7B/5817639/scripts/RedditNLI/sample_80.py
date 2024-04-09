premise = "Coca-Cola expands into coffee with $5.1 billion deal for Britain's Costa."
hypothesis = "Britain's Whitbread to sell Costa Coffee to Coke for $5.1 billion."

# extract variables from the premise and hypothesis
premise_entities = ["Coca-Cola", "Britain", "Costa"]
hypothesis_entities = ["Whitbread", "Coca-Cola", "Costa"]

# define variables for each entity
premise_variables = {"Coca-Cola": 5.1, "Britain": 1, "Costa": 1}
hypothesis_variables = {"Whitbread": 5.1, "Coca-Cola": 1, "Costa": 1}

# compare variables to determine entailment, contradiction, or neutrality
if premise_variables["Coca-Cola"]!= hypothesis_variables["Coca-Cola"]:
    label = "contradiction"
elif premise_variables["Britain"] < hypothesis_variables["Britain"]:
    label = "contradiction"
else:
    label = "entailment"

print(label)
