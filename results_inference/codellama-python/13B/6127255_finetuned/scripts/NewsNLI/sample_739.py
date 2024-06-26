votes_total_premise = 100
votes_niinisto_premise = 62.6
votes_haavisto_premise = 37.4

votes_niinisto_hypothesis = 62.6

# the hypothesis mentions the percentage of votes Niinisto gained, which is also mentioned in the premise
if votes_niinisto_hypothesis!= votes_niinisto_premise:
    # check if the percentage of votes for Niinisto in the hypothesis contradicts the percentage of votes for Niinisto in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
