more_men_snyder_premise = 4
more_men_snyder_hypothesis = 4
more_women_snyder_premise = 6
more_women_snyder_hypothesis = 6

# the hypothesis refers to the number of men and women in Snyder choir compared to Leigh choir
if more_men_snyder_hypothesis != more_men_snyder_premise:
    # check if the number of men in Snyder choir in the hypothesis contradicts the number of men in the premise
    label = "contradiction"
elif more_women_snyder_hypothesis != more_women_snyder_premise:
    # check if the number of women in Snyder choir in the hypothesis contradicts the number of women in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
