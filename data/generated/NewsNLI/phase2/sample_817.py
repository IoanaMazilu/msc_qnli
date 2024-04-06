# Premise: '' Our losses are mounting... as many as 40 military servicemen killed and over 100 wounded,'' he said.
# Hypothesis: 40 military killed and mounting civilian casualties, Georgia official says.
# Golden Label: neutral

military_killed_premise = 40
military_killed_hypothesis = 40

# the hypothesis mentions the number of military casualties, which is also mentioned in the premise
# however, the hypothesis refers to civilian casualties, which cannot be entailed from the premise
label = "neutral"

print(label)

