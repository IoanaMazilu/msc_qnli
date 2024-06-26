total_votes_premise = 6000
percent_votes_geoff_premise = 1
total_votes_hypothesis = 6000
percent_votes_geoff_hypothesis = 6

# the hypothesis refers to the same election and total votes as the premise, as well as Geoff's percentage of votes
if total_votes_premise != total_votes_hypothesis:
    # check if the total votes in the hypothesis contradicts the total votes reported in the premise
    label = "contradiction"
elif percent_votes_geoff_hypothesis >= percent_votes_geoff_premise:
    # check if the percentage of Geoff's votes in the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
