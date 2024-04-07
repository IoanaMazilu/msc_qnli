# Premise: Founded by Enzo Ferrari in less than 4928 as Scuderia Ferrari, the company sponsored drivers and manufactured race cars before moving into production of street-legal vehicles in 1947 as Ferrari S.
# Hypothesis: Founded by Enzo Ferrari in 1928 as Scuderia Ferrari, the company sponsored drivers and manufactured race cars before moving into production of street-legal vehicles in 1947 as Ferrari S.
# Golden Label: neutral

founding_year_premise = 4928
founding_year_hypothesis = 1928

# the hypothesis refers to the founding year of Ferrari, also mentioned in the premise
if founding_year_hypothesis >= founding_year_premise:
    # check if the founding year in the hypothesis contradicts the premise (which states it was founded in less than 4928)
    label = "contradiction"
else:
    # the premise gives an upper limit for the founding year
    # any year less than 'founding_year_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

