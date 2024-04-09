women_more_than_men_premise = 4
women_more_than_men_hypothesis = 6

# the hypothesis talks about the difference between the number of women and men in the board, referenced also in the premise
if women_more_than_men_hypothesis <= women_more_than_men_premise:
    # check if the hypothesis value contradicts the estimate of 'women_more_than_men_premise'
    label = "contradiction"
else:
    # if the hypothesis value is greater than the premise one, we can infer entailment
    label = "entailment"

print(label)
