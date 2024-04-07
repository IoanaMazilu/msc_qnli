# Premise: There are 4 more women than men on Centerville's board of education.
# Hypothesis: There are 1 more women than men on Centerville's board of education.
# Golden Label: contradiction

women_more_than_men_premise = 4
women_more_than_men_hypothesis = 1

# the hypothesis refers to the difference between the number of women and men on the board of education in Centerville
if women_more_than_men_hypothesis != women_more_than_men_premise:
    # check if the number of more women than men in the hypothesis contradicts the number in the premise
    label = "contradiction"
else:
    # if the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)

