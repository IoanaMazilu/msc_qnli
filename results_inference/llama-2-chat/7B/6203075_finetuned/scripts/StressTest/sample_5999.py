# The hypothesis refers to the same condition for a movie to be considered for "movie of the year" as the premise
# Compute the fraction of top-10 movies lists that the hypothesis mentions
fraction_hypothesis = 6/4

# Compare with the fraction mentioned in the premise
if fraction_hypothesis == 1/4:
    # If the fraction in the hypothesis is the same as in the premise, we can infer entailment
    label = "entailment"
elif fraction_hypothesis!= 1/4:
    # If the fraction in the hypothesis is not the same as in the premise, we can infer contradiction
    label = "contradiction"
else:
    # If the fractions are the same, we can infer neutrality
    label = "neutral"

print(label)
