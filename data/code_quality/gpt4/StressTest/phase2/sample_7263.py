women_men_diff_premise = 4
women_men_diff_hypothesis = 6

# the hypothesis refers to the difference between the number of women and men on the board, just like the premise
if women_men_diff_premise >= women_men_diff_hypothesis:
    # check if the premise value contradicts the estimate of less than 'women_men_diff_hypothesis'
    label = "contradiction"
else:
    # the hypothesis value is compatible with the premise one, but it cannot be directly inferred from the premise
    label = "neutral"

print(label)
