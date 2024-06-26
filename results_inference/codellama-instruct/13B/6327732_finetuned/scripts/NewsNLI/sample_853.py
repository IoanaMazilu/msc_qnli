likelihood_premise = 0.14
likelihood_hypothesis = 0.3

# the hypothesis mentions a higher likelihood of an attack on American soil, which contradicts the premise
if likelihood_hypothesis > likelihood_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
