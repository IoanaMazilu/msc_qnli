votes_favour_cuts_premise = 153
votes_against_cuts_premise = 128
abstentions_premise = 18
votes_favour_cuts_hypothesis = 153
votes_against_cuts_hypothesis = 128
abstentions_hypothesis = 18

# the hypothesis mentions the number of votes in favor of the cuts, opposed to the cuts, and abstentions, which are also referenced in the premise
if votes_favour_cuts_hypothesis!= votes_favour_cuts_premise or votes_against_cuts_hypothesis!= votes_against_cuts_premise or abstentions_hypothesis!= abstentions_premise:
    # check if the vote counts in the hypothesis contradict the vote counts reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
