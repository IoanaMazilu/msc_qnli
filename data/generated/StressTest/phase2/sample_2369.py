# Premise: It is rumored that in a match between 2 teams A and B, Paul picks A with the same probability as A’s chances of winning.
# Hypothesis: It is rumored that in a match between more than 2 teams A and B, Paul picks A with the same probability as A’s chances of winning.
# Golden Label: contradiction

teams_premise = 2
teams_hypothesis = 2

# the hypothesis refers to the number of teams in a match, mentioned in the premise
if teams_hypothesis != teams_premise:
    # check if the number of teams in the hypothesis contradicts the number of teams in the premise
    label = "contradiction"
else:
    # if the number of teams in the hypothesis and premise are the same, we can infer entailment
    label = "entailment"

print(label)

