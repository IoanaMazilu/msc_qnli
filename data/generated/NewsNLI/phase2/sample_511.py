# Premise: 2 person in the rebel group, Suarez had much more military experience and time served in the FARC than its leader, Cano, who was appointed to the general secretariat as the result of a deal with the Colombian communist party.
# Hypothesis: He was the No. 2 leader in the FARC guerrilla group.
# Golden Label: entailment

leader_ranking_premise = 2
leader_ranking_hypothesis = 2

# the hypothesis mentions the ranking of the person in the FARC group, which is also referenced in the premise
if leader_ranking_hypothesis != leader_ranking_premise:
    # check if the ranking in the hypothesis contradicts the ranking mentioned in the premise
    label = "contradiction"
else:
    # if the ranking in the hypothesis does not contradict the ranking in the premise, we can infer entailment
    label = "entailment"

print(label)

