# Premise: There are more than 1 more women than men on Centerville's board of education.
# Hypothesis: There are 4 more women than men on Centerville's board of education.
# Golden Label: neutral

more_women_than_men_premise = 1
more_women_than_men_hypothesis = 4

# the hypothesis talks about the difference between the number of women and men on the board, referenced also in the premise
if more_women_than_men_hypothesis <= more_women_than_men_premise:
    # check if the hypothesis value contradicts the estimate of more than 'more_women_than_men_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the difference between the number of women and men
    # any difference greater than 'more_women_than_men_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

