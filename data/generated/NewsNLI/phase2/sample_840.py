# Premise: In his backpack, police found the two planted iPads that had been in the decoy bag.
# Hypothesis: Two iPads were planted in a checked bag as part of the sting.
# Golden Label: neutral

ipads_premise = 2
ipads_hypothesis = 2

# the hypothesis mentions the number of iPads, which is also mentioned in the premise
# however, the hypothesis refers to the iPads being in a checked bag, which cannot be entailed from the premise
label = "neutral"

print(label)
