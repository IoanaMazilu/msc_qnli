women_board_premise = 4
men_board_premise = 4
women_board_hypothesis = 1
men_board_hypothesis = 1

# the hypothesis talks about the number of women and men on the board of education, referenced also in the premise
if women_board_hypothesis <= women_board_premise:
    # check if the hypothesis value contradicts the estimate of more than 'women_board_premise'
    label = "contradiction"
elif men_board_hypothesis <= men_board_premise:
    # check if the hypothesis value contradicts the estimate of more than'men_board_premise'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
