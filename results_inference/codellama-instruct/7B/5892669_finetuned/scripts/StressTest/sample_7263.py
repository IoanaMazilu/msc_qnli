women_more_than_men_premise = 4
women_more_than_men_hypothesis = 6

# the hypothesis refers to the difference in the number of women and men on the board, mentioned in the premise
if women_more_than_men_hypothesis <= women_more_than_men_premise:
    # check if the hypothesis value contradicts the number of women more than men in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
