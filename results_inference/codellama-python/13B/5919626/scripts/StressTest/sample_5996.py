women_board_premise = 4
women_board_hypothesis = 1
men_board_premise = 4
men_board_hypothesis = 1

# the hypothesis talks about the number of women and men on the board of education
# the premise gives an estimate for the number of women and men on the board of education
if women_board_premise <= women_board_hypothesis:
    # check if the hypothesis value contradicts the estimate of more than 'women_board_premise'
    label = "contradiction"
elif men_board_premise <= men_board_hypothesis:
    # check if the hypothesis value contradicts the estimate of more than'men_board_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of women and men on the board of education
    # any number of women and men greater than 'women_board_premise' and'men_board_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
