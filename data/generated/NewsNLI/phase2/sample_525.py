# Premise: At least one expert says such sites pose serious ethical questions.
# Hypothesis: One expert says open-source anti-bribe sites pose serious ethical questions.
# Golden Label: neutral

experts_premise = 1
experts_hypothesis = 1

# the hypothesis mentions one expert, which is also referenced in the premise
# however, the hypothesis refers to a specific type of sites (open-source anti-bribe), which cannot be entailed from the premise
label = "neutral"

print(label)

