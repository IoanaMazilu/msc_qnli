# Premise: Bob's pizza recipe calls for 2 ounces of baking soda for every 2 cups of flour used.
# Hypothesis: Bob's pizza recipe calls for less than 2 ounces of baking soda for every 2 cups of flour used.
# Golden Label: contradiction

baking_soda_premise = 2
baking_soda_hypothesis = 2
flour_premise = 2
flour_hypothesis = 2

# the hypothesis refers to the amount of baking soda and flour used in Bob's pizza recipe, also mentioned in the premise
if baking_soda_hypothesis >= baking_soda_premise:
    # check if the estimate of 'baking_soda_hypothesis' contradicts the amount of baking soda in the premise
    label = "contradiction"
elif flour_hypothesis != flour_premise:
    # check if the amount of flour in the hypothesis contradicts the amount of flour reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

