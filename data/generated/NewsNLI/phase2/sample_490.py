# Premise: In total, he said, more than 1,000 FBI personnel participated.
# Hypothesis: More than 1,000 FBI personnel participated in arrests.
# Golden Label: neutral

fbi_personnel_premise = 1000
fbi_personnel_hypothesis = 1000

# the hypothesis mentions the number of FBI personnel that participated, which is also referenced in the premise
# however, the hypothesis refers specifically to participation in arrests, which cannot be entailed from the premise
label = "neutral"

print(label)

