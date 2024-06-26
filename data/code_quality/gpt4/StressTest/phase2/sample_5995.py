women_more_than_men_premise = 3
women_more_than_men_hypothesis = 4

# the hypothesis talks about the number of women more than men in a board, referenced also in the premise
if women_more_than_men_hypothesis <= women_more_than_men_premise:
    # check if the hypothesis value contradicts the estimate of more than 'women_more_than_men_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of women more than men
    # any number of women more than 'women_more_than_men_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
