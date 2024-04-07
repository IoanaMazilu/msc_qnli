# Premise: There are less than 5 more women than men on Centerville's board of education.
# Hypothesis: There are 4 more women than men on Centerville's board of education.
# Golden Label: neutral

more_women_than_men_premise = 5
more_women_than_men_hypothesis = 4

# the hypothesis refers to the difference between the number of women and men in Centerville's board of education, mentioned in the premise
if more_women_than_men_hypothesis >= more_women_than_men_premise:
    # check if the difference in the hypothesis contradicts the premise's statement of 'less than more_women_than_men_premise'
    label = "contradiction"
else:
    # if the difference in the hypothesis is less than 'more_women_than_men_premise', it can be fully and explicitly entailed from the premise
    label = "entailment"

print(label)

