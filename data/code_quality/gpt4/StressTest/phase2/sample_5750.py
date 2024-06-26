rainfall_premise = 30
rainfall_hypothesis = 40

# the hypothesis talks about the total rainfall in the first two weeks of April in Springdale, also referenced in the premise
if rainfall_hypothesis == rainfall_premise:
    # check if the total rainfall in the hypothesis is the same as in the premise
    label = "entailment"
else:
    # the total rainfall in the hypothesis is different from the one reported in the premise
    label = "contradiction"

print(label)
