niinisto_votes_premise = 62.6
niinisto_votes_hypothesis = 62.6

# the hypothesis mentions the percentage of votes that Niinisto got, which is also mentioned in the premise
if niinisto_votes_hypothesis!= niinisto_votes_premise:
    # check if the number of votes for Niinisto in the hypothesis contradicts the number of votes for Niinisto reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
