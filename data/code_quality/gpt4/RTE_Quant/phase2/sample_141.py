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
