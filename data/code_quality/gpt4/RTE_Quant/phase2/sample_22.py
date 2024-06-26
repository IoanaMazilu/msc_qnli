height_premise = 8586
height_hypothesis = 8586

# the hypothesis talks about the height of Kanchenjunga, which is also mentioned in the premise
if height_hypothesis != height_premise:
    # check if the height in the hypothesis contradicts the height in the premise
    label = "contradiction"
else:
    # if the height in the hypothesis does not contradict the height in the premise, we can infer entailment
    label = "entailment"

print(label)
