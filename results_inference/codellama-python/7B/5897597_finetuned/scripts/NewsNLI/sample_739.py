niinisto_vote_premise = 62.6
niinisto_vote_hypothesis = 62.6
haavisto_vote_premise = 37.4

# the hypothesis mentions the vote percentage of Niinisto, which is also mentioned in the premise
# however, the hypothesis does not mention the vote percentage of Haavisto, which is mentioned in the premise
# thus, we cannot fully entail the hypothesis from the premise
label = "neutral"

print(label)
