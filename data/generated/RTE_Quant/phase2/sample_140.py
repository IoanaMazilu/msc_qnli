# Premise: Out of the seven expeditions who were permitted to climb the 8586-meter high Mt. Kanchenjunga, only one climber from the United States succeeded.
# Hypothesis: Kanchenjunga is 8586 meters high.
# Golden Label: entailment

expeditions_premise = 7
successful_climbers_premise = 1
mt_height_premise = 8586
mt_height_hypothesis = 8586

# the hypothesis talks about the height of Mt. Kanchenjunga which is already mentioned in the premise
# either we compare the height of the mountain in the hypothesis with the one in the premise
if mt_height_hypothesis != mt_height_premise:
    # check if the height of Mt. Kanchenjunga in the hypothesis contradicts the height in the premise
    label = "contradiction"
else:
    # if the height in the hypothesis does not contradict the height in the premise, we can infer entailment
    label = "entailment"

print(label)

