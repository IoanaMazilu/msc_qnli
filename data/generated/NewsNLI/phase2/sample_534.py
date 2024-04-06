# Premise: With numerous counts of murder, attempted murder and weapons offenses, the former doctoral student in neuroscience faces a total of 166 charges.
# Hypothesis: The former neuroscience student faces 166 charges in connection with a theater shooting.
# Golden Label: neutral

charges_premise = 166
charges_hypothesis = 166

# the hypothesis mentions the total number of charges the former student faces, which is also referenced in the premise
# however, the hypothesis refers to a theater shooting, which cannot be entailed from the premise
label = "neutral"

print(label)

