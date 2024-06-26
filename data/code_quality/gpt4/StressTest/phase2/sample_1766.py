more_men_snyder_premise = 4
more_women_snyder_premise = 6
more_men_snyder_hypothesis = 4
more_women_snyder_hypothesis = 6

# the hypothesis refers to the number of men and women Snyder has compared to Leigh, as mentioned in the premise
if more_men_snyder_hypothesis >= more_men_snyder_premise:
    # check if the 'more_men_snyder_hypothesis' contradicts the number of more men Snyder has in the premise
    label = "contradiction"
elif more_women_snyder_hypothesis >= more_women_snyder_premise:
    # check if the 'more_women_snyder_hypothesis' contradicts the number of more women Snyder has in the premise
    label = "contradiction"
else:
    # the hypothesis values do not contradict the premise ones, but they cannot be directly inferred from the premise
    label = "neutral"

print(label)
