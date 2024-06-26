votes_total = 6000
votes_percentage_premise = 1
votes_percentage_hypothesis = 7

# The hypothesis speaks about the percentage of votes Geoff received, which is also referred to in the premise
votes_geoff_premise = votes_total * (votes_percentage_premise / 100)
votes_geoff_hypothesis_max = votes_total * (votes_percentage_hypothesis / 100)

if votes_geoff_premise >= votes_geoff_hypothesis_max:
    # check if the number of votes Geoff received in the premise contradicts the hypothesis that he received less than 'votes_geoff_hypothesis_max'
    label = "contradiction"
else:
    # if the number of votes Geoff received according to the premise doesn't contradict the hypothesis, we infer entailment
    label = "entailment"

print(label)
