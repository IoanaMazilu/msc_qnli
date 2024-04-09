molinari_birdies_premise = 6
molinari_birdies_hypothesis = 11
molinari_score_premise = 65
molinari_score_hypothesis = 65

# the hypothesis mentions Molinari's score and the number of birdies he made, which are also mentioned in the premise
if molinari_birdies_hypothesis!= molinari_birdies_premise:
    # check if the number of birdies in the hypothesis contradicts the number of birdies reported in the premise
    label = "contradiction"
elif molinari_score_hypothesis!= molinari_score_premise:
    # check if the score from the hypothesis contradicts the score in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
