# Premise: Founded by Enzo Ferrari in 1928 as Scuderia Ferrari, the company sponsored drivers and manufactured race cars before moving into production of street-legal vehicles in 1947 as Ferrari S.
# Hypothesis: Founded by Enzo Ferrari in less than 4928 as Scuderia Ferrari, the company sponsored drivers and manufactured race cars before moving into production of street-legal vehicles in 1947 as Ferrari S.
# Golden Label: entailment

founding_year_premise = 1928
founding_year_hypothesis = 4928

# the hypothesis talks about the founding year of Scuderia Ferrari, which is also mentioned in the premise
if founding_year_hypothesis <= founding_year_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # the founding year in the hypothesis does not contradict the founding year in the premise
    # but, it cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

