votes_counted_premise = 100
votes_counted_hypothesis = 100
niinisto_vote_premise = 0.626
niinisto_vote_hypothesis = 0.626
haavisto_vote_premise = 0.374
haavisto_vote_hypothesis = 0.374

# the hypothesis mentions the vote percentage for Niinisto and Haavisto, which are also mentioned in the premise
if niinisto_vote_hypothesis!= niinisto_vote_premise:
    # check if the vote percentage for Niinisto in the hypothesis contradicts the vote percentage for Niinisto in the premise
    label = "contradiction"
elif haavisto_vote_hypothesis!= haavisto_vote_premise:
    # check if the vote percentage for Haavisto in the hypothesis contradicts the vote percentage for Haavisto in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
