women_on_board_premise = 4
men_on_board_premise = 4 + 4
women_on_board_hypothesis = 1
men_on_board_hypothesis = 1 + 1

# the hypothesis refers to the number of women and men on the board of education
if women_on_board_hypothesis <= women_on_board_premise:
    # check if the hypothesis value contradicts the estimate of 'women_on_board_premise'
    label = "contradiction"
elif men_on_board_hypothesis!= men_on_board_premise:
    # check if the number of men on the board in the hypothesis contradicts the number of men reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
