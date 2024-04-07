# Premise: If Snyder has less than 7 more men and 6 more women than Leigh, how many men are in the Snyder choir?
# Hypothesis: If Snyder has 4 more men and 6 more women than Leigh, how many men are in the Snyder choir?
# Golden Label: neutral

more_men_snyder_premise = 7
more_men_snyder_hypothesis = 4
more_women_snyder_premise = 6
more_women_snyder_hypothesis = 6

# the hypothesis refers to the number of more men and women in Snyder as compared to Leigh mentioned in the premise
if more_men_snyder_premise < more_men_snyder_hypothesis:
    # check if the number of 'more_men_snyder_hypothesis' contradicts the number of more men in Snyder choir in the premise
    label = "contradiction"
elif more_women_snyder_hypothesis != more_women_snyder_premise:
    # check if the number of more women in Snyder choir in the hypothesis contradicts the number of more women reported in the premise
    label = "contradiction"
elif more_men_snyder_premise > more_men_snyder_hypothesis:
    # check if the number of 'more_men_snyder_hypothesis' can be fully and explicitly entailed from the number of more men in Snyder choir in the premise
    label = "entailment"
else:
    # if the hypothesis values do not contradict the premise ones and also cannot be fully and explicitly entailed, we infer neutral
    label = "neutral"

print(label)

