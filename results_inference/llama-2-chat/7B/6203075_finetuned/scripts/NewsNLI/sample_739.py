vote_percentage_niinisto_premise = 62.6
vote_percentage_niinisto_hypothesis = 62.6

# the hypothesis mentions the percentage of votes gained by Niinisto, which is also mentioned in the premise
if vote_percentage_niinisto_hypothesis!= vote_percentage_niinisto_premise:
    # check if the percentage of votes gained by Niinisto in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
else:
    # if the percentage of votes gained by Niinisto in the hypothesis does not contradict the percentage in the premise, we can infer entailment
    label = "entailment"

print(label)
