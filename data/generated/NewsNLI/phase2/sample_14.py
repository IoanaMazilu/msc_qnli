# Premise: Sotomayor was easily confirmed in a 68-31 vote.
# Hypothesis: Sonia Sotomayor wins confirmation by 68-31 vote.
# Golden Label: entailment

votes_for_sotomayor_premise = 68
votes_against_sotomayor_premise = 31
votes_for_sotomayor_hypothesis = 68
votes_against_sotomayor_hypothesis = 31

# the hypothesis mentions the vote counts for and against Sotomayor, which are also mentioned in the premise
if votes_for_sotomayor_hypothesis != votes_for_sotomayor_premise:
    # check if the vote count for Sotomayor in the hypothesis contradicts the vote count for Sotomayor in the premise
    label = "contradiction"
elif votes_against_sotomayor_hypothesis != votes_against_sotomayor_premise:
    # check if the vote count against Sotomayor from the hypothesis contradicts the vote count against Sotomayor in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

