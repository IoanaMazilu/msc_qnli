more_women_than_men_premise = 4
more_women_than_men_hypothesis = 6

# the hypothesis refers to the difference in number of women and men on Centerville's board of education mentioned in the premise
if more_women_than_men_premise >= more_women_than_men_hypothesis:
    # check if the estimate of'more_women_than_men_hypothesis' contradicts the number of more women than men in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
