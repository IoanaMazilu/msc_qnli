votes_premise = 6000
votes_hypothesis = 6000
percent_votes_geoff_premise = 6
percent_votes_geoff_hypothesis = 1

# the hypothesis refers to the same election and candidate Geoff mentioned in the premise
if votes_hypothesis != votes_premise:
    # check if the number of votes in the hypothesis contradicts the number of votes reported in the premise
    label = "contradiction"
elif percent_votes_geoff_hypothesis >= percent_votes_geoff_premise:
    # check if the percentage of votes for Geoff in the hypothesis contradicts the percentage of votes for Geoff in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of votes for Geoff
    # any percentage of votes less than 'percent_votes_geoff_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
