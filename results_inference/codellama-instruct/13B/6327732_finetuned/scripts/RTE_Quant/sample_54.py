exports_premise = 1.44e12
imports_premise = 2.2e12
exports_hypothesis = 1.44e12 * 1.105
imports_hypothesis = 2.2e12 * 1.105

# the hypothesis talks about the percentage change in exports and imports, which are not mentioned in the premise
# the hypothesis cannot be entailed from the premise, since the percentage change in exports and imports is unknown.
label = "neutral"

print(label)
