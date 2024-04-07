# Premise: Bob's pizza recipe calls for 2 ounces of baking soda for every 2 cups of flour used.
# Hypothesis: Bob's pizza recipe calls for less than 8 ounces of baking soda for every 2 cups of flour used.
# Golden Label: entailment

baking_soda_premise = 2
baking_soda_hypothesis = 8
flour_premise = 2
flour_hypothesis = 2

# the hypothesis mentions the amount of baking soda per 2 cups of flour in Bob's pizza recipe, as indicated in the premise
if baking_soda_hypothesis <= baking_soda_premise:
    # check if the hypothesis value contradicts the amount of baking soda used in the premise
    label = "contradiction"
elif flour_hypothesis != flour_premise:
    # check if the amount of flour used in the hypothesis contradicts the amount of flour used in the premise
    label = "contradiction"
else:
    # the hypothesis value of baking soda does not contradict the premise and can be fully entailed from it
    label = "entailment"

print(label)

