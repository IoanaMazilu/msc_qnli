# Premise: If Snyder has 4 more men and 6 more women than Leigh, how many men's are in the Snyder choir?
# Hypothesis: If Snyder has less than 5 more men and 6 more women than Leigh, how many men's are in the Snyder choir?
# Golden Label: entailment

more_men_snyder_premise = 4
more_men_snyder_hypothesis = 5

# the hypothesis talks about the difference in the number of men in Snyder's choir compared to Leigh, referenced also in the premise
if more_men_snyder_hypothesis <= more_men_snyder_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # the hypothesis does not provide an exact number, but a boundary
    # the premise number falls within this boundary, so it does not contradict the hypothesis, but cannot be explicitly entailed either
    label = "neutral"

print(label)

