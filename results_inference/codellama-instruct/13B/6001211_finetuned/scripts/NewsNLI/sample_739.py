niinisto_votes_premise = 0.626
haavisto_votes_premise = 0.374
niinisto_votes_hypothesis = 0.626

# the hypothesis mentions the percentage of votes Niinisto gained, which is also mentioned in the premise
if niinisto_votes_hypothesis!= niinisto_votes_premise:
    # check if the percentage of votes for Niinisto in the hypothesis contradicts the percentage of votes for Niinisto in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
