# Premise: According to Finland's Ministry of Justice, with 100% of votes counted, Niinisto defeated the nation's first openly gay presidential candidate, Pekka Haavisto, with 62.6% of the vote compared to Haavisto's 37.4%.
# Hypothesis: Sauli Niinisto gained 62.6% of the vote, preliminary results show.
# Golden Label: neutral

niinisto_vote_percentage_premise = 62.6
niinisto_vote_percentage_hypothesis = 62.6

# the hypothesis mentions the vote percentage of Niinisto, which is also referenced in the premise
if niinisto_vote_percentage_hypothesis != niinisto_vote_percentage_premise:
    # check if the vote percentage for Niinisto in the hypothesis contradicts the vote percentage reported in the premise
    label = "contradiction"
else:
    # if the vote percentage for Niinisto in the hypothesis does not contradict the vote percentage in the premise, we can infer entailment
    label = "entailment"

print(label)

