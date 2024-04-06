# Premise: The association says there are 2,000 for-profit haunts across the country, plus another 1,000 houses run for charity.
# Hypothesis: About a third of the 3,000 houses in the United States benefit charity, group says.
# Golden Label: entailment

profit_haunts_premise = 2000
charity_haunts_premise = 1000
total_haunts_premise = profit_haunts_premise + charity_haunts_premise

total_haunts_hypothesis = 3000
charity_haunts_hypothesis = total_haunts_hypothesis / 3

# The hypothesis mentions the total number of houses in the U.S. and the number of houses that benefit charity, 
# which are also referenced in the premise
if total_haunts_hypothesis != total_haunts_premise:
    # check if the total number of houses in the hypothesis contradicts the total number of houses in the premise
    label = "contradiction"
elif charity_haunts_hypothesis != charity_haunts_premise:
    # check if the number of charity houses in the hypothesis contradicts the number of charity houses in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

