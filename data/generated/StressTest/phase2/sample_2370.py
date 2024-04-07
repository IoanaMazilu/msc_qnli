# Premise: Let’s assume such rumors to be true and that in a match between Ghana and Bolivia ; Ghana the stronger team has a probability of 2/3 of winning the game.
# Hypothesis: Let’s assume such rumors to be true and that in a match between Ghana and Bolivia ; Ghana the stronger team has a probability of less than 8/3 of winning the game.
# Golden Label: entailment

winning_probability_premise = 2/3
winning_probability_hypothesis = 8/3

# the hypothesis talks about the winning probability of Ghana, a fact also mentioned in the premise
if winning_probability_hypothesis <= winning_probability_premise:
    # check if the hypothesis value contradicts the actual winning probability of Ghana in the premise
    label = "contradiction"
else:
    # the premise gives the actual winning probability of Ghana
    # if the hypothesis value does not contradict the premise value, then we can infer entailment
    label = "entailment"

print(label)

