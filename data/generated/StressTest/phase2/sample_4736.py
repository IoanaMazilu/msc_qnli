# Premise: If Snyder has 4 more men and 6 more women than Leigh, how many men are in the Snyder choir?
# Hypothesis: If Snyder has 2 more men and 6 more women than Leigh, how many men are in the Snyder choir?
# Golden Label: contradiction

men_more_snyder_premise = 4
men_more_snyder_hypothesis = 2
women_more_snyder_premise = 6
women_more_snyder_hypothesis = 6

# the hypothesis refers to the number of men and women in Snyder's choir compared to Leigh's choir
if men_more_snyder_premise != men_more_snyder_hypothesis:
    # check if the number of more men in Snyder's choir in the hypothesis contradicts the premise
    label = "contradiction"
elif women_more_snyder_premise != women_more_snyder_hypothesis:
    # check if the number of more women in Snyder's choir in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if none of the hypothesis values contradicts the premise values, we infer neutrality
    # since we do not have the exact number of men in the Snyder choir in either premise or hypothesis
    label = "neutral"

print(label)

