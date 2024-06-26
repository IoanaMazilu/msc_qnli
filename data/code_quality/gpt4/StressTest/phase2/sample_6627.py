lowest_score_premise = 1
lowest_score_hypothesis = 8

# the hypothesis refers to the lowest score Mary got in the game, which is also mentioned in the premise
if lowest_score_hypothesis < lowest_score_premise:
    # check if the 'lowest_score_hypothesis' contradicts the 'lowest_score_premise'
    label = "contradiction"
elif lowest_score_hypothesis == lowest_score_premise:
    # if the lowest scores are the same, we can infer entailment
    label = "entailment"
else:
    # if the 'lowest_score_hypothesis' is greater than the 'lowest_score_premise', 
    # it does not contradict the premise, but cannot be entailed from it either
    label = "neutral"

print(label)
