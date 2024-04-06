# Premise: A recipe calls for 18.0 servings of cereal and each serving is 2.0 cups.
# Hypothesis: 36.0 cups are needed.
# Golden Label: entailment

servings_premise = 18.0
cups_per_serving_premise = 2.0
total_cups_hypothesis = 36.0

# the hypothesis refers to the total number of cups, which can be calculated from the premise
# compute the total number of cups in the premise
total_cups_premise = servings_premise * cups_per_serving_premise
if total_cups_hypothesis != total_cups_premise:
    # check if the number of cups in the hypothesis contradicts the number of cups calculated from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

