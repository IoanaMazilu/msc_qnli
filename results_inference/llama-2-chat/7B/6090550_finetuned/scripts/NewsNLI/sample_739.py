vote_percentage_niinisto_premise = 62.6
vote_percentage_niinisto_hypothesis = 62.6

# the hypothesis mentions the vote percentage of Sauli Niinisto, which is also mentioned in the premise
if vote_percentage_niinisto_hypothesis!= vote_percentage_niinisto_premise:
    # check if the vote percentage in the hypothesis contradicts the vote percentage in the premise
    label = "contradiction"
else:
    # if the vote percentage in the hypothesis matches the vote percentage in the premise, we can infer entailment
    label = "entailment"

print(label)
