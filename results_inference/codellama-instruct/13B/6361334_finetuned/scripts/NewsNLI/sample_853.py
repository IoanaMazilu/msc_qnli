likelihood_premise = 0.14
likelihood_hypothesis = 0.3

# the hypothesis mentions the likelihood of a terrorist attack in the US, which is also mentioned in the premise
# however, the hypothesis mentions a higher likelihood of an attack, which cannot be entailed from the premise
label = "contradiction"

print(label)
