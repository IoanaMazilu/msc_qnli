charities_premise = 3
board_members_premise = 4
board_members_hypothesis = 8

# the hypothesis talks about the number of board members for each charity, referenced also in the premise
if board_members_hypothesis <= board_members_premise:
    # check if the hypothesis value contradicts the estimate of more than 'board_members_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of board members
    # any number of board members greater than 'board_members_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
