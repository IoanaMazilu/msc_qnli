women_premise = 4
men_premise = 4
women_hypothesis = 1

# the hypothesis talks about the number of women and men on Centerville's board of education, referenced also in the premise
if women_hypothesis <= women_premise:
    # check if the hypothesis value contradicts the estimate of more than 'women_premise' women on the board
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of women
    # any number of women greater than 'women_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
