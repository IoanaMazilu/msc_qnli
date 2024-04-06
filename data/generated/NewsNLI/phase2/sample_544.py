# Premise: Mexico City (CNN) -- Mexican authorities say they've arrested three additional suspects connected to the kidnapping of 13 youths from a bar in the country's capital.
# Hypothesis: Federal prosecutors say they arrested three additional suspects.
# Golden Label: neutral

suspects_arrested_premise = 3
suspects_arrested_hypothesis = 3

# the hypothesis mentions the number of suspects arrested, which is also mentioned in the premise
if suspects_arrested_hypothesis != suspects_arrested_premise:
    # check if the number of suspects arrested in the hypothesis contradicts the number of suspects arrested in the premise
    label = "contradiction"
else:
    # if the number of suspects arrested in the hypothesis does not contradict the number of suspects arrested in the premise, we can infer entailment
    label = "entailment"

print(label)

