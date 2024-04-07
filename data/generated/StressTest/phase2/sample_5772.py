# Premise: There are 4 more women than men on Centerville's board of education.
# Hypothesis: There are less than 7 more women than men on Centerville's board of education.
# Golden Label: entailment

women_more_than_men_premise = 4
women_more_than_men_hypothesis = 7

# the hypothesis refers to the difference in the number of women and men on the board, which is also mentioned in the premise
if women_more_than_men_hypothesis <= women_more_than_men_premise:
    # check if the hypothesis value contradicts the specific number of 'women_more_than_men_premise'
    label = "contradiction"
else:
    # the premise gives the exact difference in the number of women and men
    # any number of women more than men less than 'women_more_than_men_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

