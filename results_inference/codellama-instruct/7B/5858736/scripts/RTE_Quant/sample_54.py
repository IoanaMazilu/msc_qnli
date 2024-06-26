# Define variables for the numerical entities in the premise and hypothesis
exports_premise = 1.44e12
imports_premise = 2.2e12
exports_hypothesis = 1.05e12

# Extract all quantities as valid numbers
exports_premise = float(exports_premise)
imports_premise = float(imports_premise)
exports_hypothesis = float(exports_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
if exports_hypothesis!= exports_premise:
    # Check if the number of exports in the hypothesis contradicts the number of exports from the premise
    label = "contradiction"
elif imports_premise!= imports_hypothesis:
    # Check if the number of imports in the hypothesis contradicts the number of imports from the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
