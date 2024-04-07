# Premise: How many hours does it take Little Texas Drilling Company to produce 205 barrels of oil?
# Hypothesis: How many hours does it take Little Texas Drilling Company to produce more than 205 barrels of oil?
# Golden Label: contradiction

oil_prod_premise = 205
oil_prod_hypothesis = 205

# The hypothesis talks about the number of barrels of oil produced by Little Texas Drilling Company, which is also referenced in the premise.
if oil_prod_hypothesis != oil_prod_premise:
    # Check if the number of barrels in the hypothesis contradicts the number of barrels reported in the premise.
    label = "contradiction"
else:
    # If the quantity of oil in the hypothesis does not contradict the premise, we can infer entailment.
    label = "entailment"

print(label)

