# Premise: There are 4 more women than men on Centerville's board of education.
# Hypothesis: There are more than 3 more women than men on Centerville's board of education.
# Golden Label: entailment

women_more_than_men_premise = 4
women_more_than_men_hypothesis = 3

# the hypothesis refers to the number of women more than men in Centerville's board of education mentioned in the premise
if women_more_than_men_hypothesis >= women_more_than_men_premise:
    # check if the hypothesis value contradicts the number of women more than men in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

