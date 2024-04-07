# Premise: Founded by Enzo Ferrari in 1928 as Scuderia Ferrari, the company sponsored drivers and manufactured race cars before moving into production of street-legal vehicles in 1947 as Ferrari S.
# Hypothesis: Founded by Enzo Ferrari in 6928 as Scuderia Ferrari, the company sponsored drivers and manufactured race cars before moving into production of street-legal vehicles in 1947 as Ferrari S.
# Golden Label: contradiction

founding_year_premise = 1928
founding_year_hypothesis = 6928

# The hypothesis talks about the founding year of Scuderia Ferrari, also mentioned in the premise
if founding_year_hypothesis != founding_year_premise:
    # Check if the founding year in the hypothesis contradicts the founding year mentioned in the premise
    label = "contradiction"
else:
    # If the founding year in the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)

