# Premise: A cereal box holds 18.0 cups of cereal and each serving is 2.0 cups.
# Hypothesis: 9.0 servings are in the whole box.
# Golden Label: entailment

total_cups_premise = 18.0
serving_cups_premise = 2.0
servings_hypothesis = 9.0

# The hypothesis refers to the total number of servings, which can be computed from the premise
# Calculate the total number of servings in the premise
total_servings_premise = total_cups_premise / serving_cups_premise
if total_servings_premise != servings_hypothesis:
    # Check if the number of servings in the hypothesis contradicts the number of servings from the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

