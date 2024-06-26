board_members_premise = 4
board_members_hypothesis = 8

# the hypothesis refers to the number of board members in each of three charities, also mentioned in the premise
if board_members_hypothesis <= board_members_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value is greater than the premise value, it is entailed by the premise
    label = "entailment"

print(label)
