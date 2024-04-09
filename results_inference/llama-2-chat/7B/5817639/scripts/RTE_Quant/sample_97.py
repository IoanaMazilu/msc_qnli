asteroid_diameter_premise = 100
asteroid_diameter_hypothesis = 100

# the hypothesis talks about the diameter of an asteroid, which is also mentioned in the premise
if asteroid_diameter_hypothesis == asteroid_diameter_premise:
    # if the hypothesis and premise values match, we can infer entailment
    label = "entailment"
elif asteroid_diameter_hypothesis > asteroid_diameter_premise:
    # if the hypothesis value is greater than the premise value, we can infer entailment
    label = "entailment"
elif asteroid_diameter_hypothesis < asteroid_diameter_premise:
    # if the hypothesis value is less than the premise value, we can infer contradiction
    label = "contradiction"
else:
    # if the hypothesis and premise values do not match or are equal, we can infer neutrality
    label = "neutral"

print(label)
