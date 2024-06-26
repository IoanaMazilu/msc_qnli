exports_premise = 1.44e12
exports_hypothesis = 1.44e12 * 1.105

# the hypothesis talks about the percentage increase of exports, which is not mentioned in the premise
# the hypothesis cannot be entailed from the premise, since the percentage increase of exports is unknown.
label = "neutral"

print(label)
