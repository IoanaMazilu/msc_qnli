# Premise: There are 4 more women than men on Centerville's board of education.
# Hypothesis: There are less than 5 more women than men on Centerville's board of education.
# Golden Label: entailment

women_more_than_men_premise = 4
women_more_than_men_hypothesis = 5

# the hypothesis discusses the difference in number of women and men on Centerville's board, also mentioned in the premise
if women_more_than_men_premise >= women_more_than_men_hypothesis:
    # check if the number of women more than men in the premise contradicts the hypothesis
    label = "contradiction"
else:
    # if the difference (number of women more than men) in the premise does not contradict the hypothesis, we can infer entailment
    label = "entailment"

print(label)

