# Premise: A dust storm sweeps across the prairie and it covers 64535.0 acres of the prairie in the dust, and leaves 522.0 acres untouched.
# Hypothesis: 65057.0 acres are in the prarie.
# Golden Label: entailment

covered_acres_premise = 64535.0
untouched_acres_premise = 522.0
total_acres_hypothesis = 65057.0

# The hypothesis refers to the total number of acres in the prairie, which can be inferred from the premise
# Compute the total number of acres in the premise
total_acres_premise = covered_acres_premise + untouched_acres_premise

if total_acres_hypothesis != total_acres_premise:
    # Check if the total acres from the hypothesis contradicts the total acres from the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

