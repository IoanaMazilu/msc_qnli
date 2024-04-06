# Premise: A seven-member Tibetan mountaineering team conquered the 8,586-meter Mt. Kanchenjunga, the third highest peak of the world, the Chinese mountaineering association confirmed here on Sunday.
# Hypothesis: Kanchenjunga is 8586 meters high.
# Golden Label: entailment

height_premise = 8586
height_hypothesis = 8586

# the hypothesis talks about the height of the mountain, which is also mentioned in the premise
if height_hypothesis != height_premise:
    # check if the height in the hypothesis contradicts the height in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

