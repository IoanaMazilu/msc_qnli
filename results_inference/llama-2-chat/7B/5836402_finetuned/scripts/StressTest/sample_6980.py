charities_premise = 3
board_members_premise = 8
board_members_hypothesis = 8

# the hypothesis refers to the number of board members of each charity in Novel Grove Estates, also mentioned in the premise
if board_members_hypothesis <= board_members_premise:
    # check if the estimate of 'board_members_hypothesis' contradicts the number of board members in the premise
    label = "contradiction"
elif charities_hypothesis!= charities_premise:
    # check if the number of charities in the hypothesis contradicts the number of charities reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
