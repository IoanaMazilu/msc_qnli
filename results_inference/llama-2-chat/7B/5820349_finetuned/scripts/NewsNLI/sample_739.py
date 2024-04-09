niinisto_vote_premise = 62.6
haavisto_vote_premise = 37.4
niinisto_vote_hypothesis = 62.6
haavisto_vote_hypothesis = 37.4

# the hypothesis mentions the vote percentage of Niinisto and Haavisto, which are also mentioned in the premise
if niinisto_vote_hypothesis!= niinisto_vote_premise:
    # check if the vote percentage of Niinisto in the hypothesis contradicts the vote percentage of Niinisto reported in the premise
    label = "contradiction"
elif haavisto_vote_hypothesis!= haavisto_vote_premise:
    # check if the vote percentage of Haavisto from the hypothesis contradicts the vote percentage of Haavisto in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
