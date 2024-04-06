# Premise: Mexican authorities accused four top military officials of connections with organized crime in a high-profile case that has renewed debate over the role of government troops in the drug war.
# Hypothesis: Four top military officials are in a maximum-security prison.
# Golden Label: neutral

officials_premise = 4
officials_hypothesis = 4

# the number of military officials mentioned in the hypothesis is the same as in the premise
# however, the hypothesis makes a claim that the officials are in a maximum-security prison, which cannot be entailed from the premise
label = "neutral"

print(label)

