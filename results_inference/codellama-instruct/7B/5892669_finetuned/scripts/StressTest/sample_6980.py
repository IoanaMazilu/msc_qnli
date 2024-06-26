board_members_premise = 8
board_members_hypothesis = 8

# the hypothesis refers to the number of board members in each charity mentioned in the premise
if board_members_hypothesis <= board_members_premise:
    # check if the hypothesis value contradicts the exact number of board members in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
