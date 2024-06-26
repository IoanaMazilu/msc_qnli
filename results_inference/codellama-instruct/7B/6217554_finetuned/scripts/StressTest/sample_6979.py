charities_premise = 3
charities_hypothesis = 3
persons_board_directors_premise = 4
persons_board_directors_hypothesis = 8

# the hypothesis talks about the number of persons serving on the board of directors of each charity, referenced also in the premise
if persons_board_directors_hypothesis <= persons_board_directors_premise:
    # check if the number of persons serving on the board of directors in the hypothesis contradicts the estimate of more than 'persons_board_directors_premise'
    label = "contradiction"
elif charities_hypothesis!= charities_premise:
    # check if the number of charities in the hypothesis contradicts the number of charities reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
