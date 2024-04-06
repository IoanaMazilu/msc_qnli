# Premise: Miami (CNN) -- A Florida sheriff who just arrested 22 men caught in an online undercover operation blames the policies of the Internet sites used by sexual predators.
# Hypothesis: 22 men from at least 4 states arrested in Florida.
# Golden Label: neutral

arrested_men_premise = 22
arrested_men_hypothesis = 22

# the hypothesis mentions the number of men arrested in Florida, which is also referenced in the premise
# however, the hypothesis refers to the states those men come from, which cannot be entailed from the premise
label = "neutral"

print(label)

