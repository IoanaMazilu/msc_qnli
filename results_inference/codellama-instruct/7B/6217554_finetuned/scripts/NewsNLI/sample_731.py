birdies_premise = 6
birdies_hypothesis = 6
round_score_premise = 65
round_score_hypothesis = 65

# the hypothesis mentions the number of birdies and the round score of Molinari, which are also mentioned in the premise
if birdies_hypothesis!= birdies_premise:
    # check if the number of birdies from the hypothesis contradicts the number of birdies in the premise
    label = "contradiction"
elif round_score_hypothesis!= round_score_premise:
    # check if the round score from the hypothesis contradicts the round score in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
