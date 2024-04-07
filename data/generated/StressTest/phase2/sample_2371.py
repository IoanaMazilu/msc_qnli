# Premise: Let’s assume such rumors to be true and that in a match between Ghana and Bolivia ; Ghana the stronger team has a probability of less than 8/3 of winning the game.
# Hypothesis: Let’s assume such rumors to be true and that in a match between Ghana and Bolivia ; Ghana the stronger team has a probability of 2/3 of winning the game.
# Golden Label: neutral

winning_probability_premise = 8/3
winning_probability_hypothesis = 2/3

# the hypothesis talks about the winning probability of Ghana, referenced also in the premise
if winning_probability_hypothesis >= winning_probability_premise:
    # check if the hypothesis value contradicts the estimate of less than 'winning_probability_premise'
    label = "contradiction"
elif winning_probability_hypothesis == winning_probability_premise:
    # if the values are equal, it also contradicts the premise because it specifically mentioned less than 'winning_probability_premise'
    label = "contradiction"
else:
    # any winning probability less than 'winning_probability_premise' is consistent with the premise, thus it can be explicitly entailed from the premise
    label = "entailment"

print(label)

