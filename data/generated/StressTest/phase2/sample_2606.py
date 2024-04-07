# Premise: The ratio of men to women in the Snyder community choir is 4 to 6.
# Hypothesis: The ratio of men to women in the Snyder community choir is less than 4 to 6.
# Golden Label: contradiction

men_women_premise = 4/6
men_women_hypothesis = 4/6

# the hypothesis talks about the ratio of men to women in the choir, which is also mentioned in the premise
if men_women_hypothesis < men_women_premise:
    # check if the hypothesis ratio is less than the premise ratio
    label = "entailment"
elif men_women_hypothesis == men_women_premise:
    # check if the hypothesis ratio is equal to the premise ratio
    label = "contradiction"
else:
    # if the hypothesis ratio is neither less than nor equal to the premise ratio, it can't be entailed or contradicted by the premise
    label = "neutral"

print(label)

