# Premise: Police said there were three people on board:the pilot and two passengers.
# Hypothesis: 3 people on board.
# Golden Label: entailment

people_on_board_premise = 3
people_on_board_hypothesis = 3

# the hypothesis mentions the number of people on board, which is also mentioned in the premise
if people_on_board_hypothesis != people_on_board_premise:
    # check if the number of people in the hypothesis contradicts the number of people in the premise
    label = "contradiction"
else:
    # if the number of people from the hypothesis does not contradict the number of people in the premise, we can infer entailment
    label = "entailment"

print(label)

