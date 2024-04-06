# Premise: Robin Van Persie scored four as the Netherlands put San Marino to the sword with an 11-0 thrashing.
# Hypothesis: Robin Van Persie scores four as Netherlands destroy San Marino 11-0.
# Golden Label: entailment

persie_goals_premise = 4
persie_goals_hypothesis = 4
netherlands_score_premise = 11
netherlands_score_hypothesis = 11

# the hypothesis mentions the number of goals scored by Robin Van Persie and the final score of the Netherlands team, which are also mentioned in the premise
if persie_goals_hypothesis != persie_goals_premise:
    # check if the number of goals by Persie in the hypothesis contradicts the number of goals he scored according to the premise
    label = "contradiction"
elif netherlands_score_hypothesis != netherlands_score_premise:
    # check if the final score of the Netherlands team from the hypothesis contradicts the final score in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

