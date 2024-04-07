# Premise: If Snyder has more than 3 more men and 6 more women than Leigh, how many women are in the Snyder choir?
# Hypothesis: If Snyder has 4 more men and 6 more women than Leigh, how many women are in the Snyder choir?
# Golden Label: neutral

men_more_snyder_premise = 3
men_more_snyder_hypothesis = 4
women_more_snyder_premise = 6
women_more_snyder_hypothesis = 6

# the hypothesis refers to the number of more men and women Snyder has than Leigh, mentioned in the premise
if men_more_snyder_hypothesis <= men_more_snyder_premise:
    # check if the number in 'men_more_snyder_hypothesis' contradicts the estimate of more men in the premise
    label = "contradiction"
elif women_more_snyder_hypothesis != women_more_snyder_premise:
    # check if the number of more women in the hypothesis contradicts the number of more women in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

