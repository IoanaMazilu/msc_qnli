# Premise: In England's Premier League, unbeaten Newcastle moved up to fourth place despite being held 0-0 away to promoted Queen's Park Rangers.
# Hypothesis: Unbeaten Newcastle move up to fourth place in England after 0-0 draw at promoted QPR.
# Golden Label: entailment

newcastle_position_premise = 4
newcastle_position_hypothesis = 4
match_result_premise = 0
match_result_hypothesis = 0

# the hypothesis mentions Newcastle's position and the match result, which are also mentioned in the premise
if newcastle_position_hypothesis != newcastle_position_premise:
    # check if the position of Newcastle in the hypothesis contradicts the position reported in the premise
    label = "contradiction"
elif match_result_hypothesis != match_result_premise:
    # check if the match result from the hypothesis contradicts the match result in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
