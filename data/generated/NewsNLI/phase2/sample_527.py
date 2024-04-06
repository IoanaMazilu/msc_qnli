# Premise: A kilogram fetches about $20,000 -- with a single horn weighing about 10 kilograms (22 pounds).
# Hypothesis: A kilogram fetches about $20,000, experts say.
# Golden Label: neutral

price_per_kg_premise = 20000
price_per_kg_hypothesis = 20000

# the hypothesis mentions the price per kilogram, which is also mentioned in the premise
if price_per_kg_hypothesis != price_per_kg_premise:
    # check if the price per kilogram in the hypothesis contradicts the price per kilogram reported in the premise
    label = "contradiction"
else:
    # if the price per kilogram in the hypothesis does not contradict the price per kilogram in the premise, we can infer entailment
    label = "entailment"

print(label)

