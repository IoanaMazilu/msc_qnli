women_more_than_men_premise = 7
women_more_than_men_hypothesis = 4

# the hypothesis refers to the number of women more than men on the board, which is also mentioned in the premise
if women_more_than_men_hypothesis >= women_more_than_men_premise:
    # check if the number of 'women_more_than_men_hypothesis' contradicts the estimate of less than 'women_more_than_men_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the difference between women and men
    # any number less than 'women_more_than_men_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
