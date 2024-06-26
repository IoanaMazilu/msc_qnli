mountain_height_premise = 8586
mountain_height_hypothesis = 8586

# the hypothesis makes a claim about the height of Kanchenjunga, which is also mentioned in the premise
if mountain_height_hypothesis != mountain_height_premise:
    # check if the height of the mountain in the hypothesis contradicts the height of the mountain in the premise
    label = "contradiction"
else:
    # if the height of the mountain in the hypothesis does not contradict the height of the mountain in the premise, we can infer entailment
    label = "entailment"

print(label)
