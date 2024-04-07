# Premise: Shaquan has 5 playing cards, each one is ordered by the number on it, but one card is flipped over. They are numbered 8, 16, 24, x, 40.
# Hypothesis: Shaquan has more than 3 playing cards, each one is ordered by the number on it, but one card is flipped over. They are numbered 8, 16, 24, x, 40.
# Golden Label: entailment

cards_premise = 5
cards_hypothesis = 3

# The hypothesis refers to the number of Shaquan's playing cards mentioned in the premise
if cards_hypothesis >= cards_premise:
    # Check if the number of cards in the hypothesis contradicts the number of cards reported in the premise
    label = "contradiction"
else:
    # If the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
