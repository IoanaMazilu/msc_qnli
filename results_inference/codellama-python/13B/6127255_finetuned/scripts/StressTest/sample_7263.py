women_more_than_men_premise = 4
women_more_than_men_hypothesis = 6

# the hypothesis refers to the number of women more than men in Centerville's board of education, as mentioned in the premise
if women_more_than_men_premise >= women_more_than_men_hypothesis:
    # check if the number of women more than men in the premise contradicts the hypothesis
    label = "contradiction"
else:
    # if the number of women more than men in the premise does not contradict the hypothesis, we can infer entailment
    label = "entailment"

print(label)
