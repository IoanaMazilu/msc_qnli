women_more_men = 4
women_more_men_hypothesis = 6

# the hypothesis refers to the difference between women and men on the board of education
if women_more_men > women_more_men_hypothesis:
    # check if the difference in the premise contradicts the hypothesis
    label = "contradiction"
elif women_more_men < women_more_men_hypothesis:
    # if the difference in the premise is less than the hypothesis, it does not contradict the hypothesis
    label = "neutral"
else:
    # if the difference in the premise is equal to the hypothesis, it does not contradict the hypothesis
    label = "neutral"

print(label)
