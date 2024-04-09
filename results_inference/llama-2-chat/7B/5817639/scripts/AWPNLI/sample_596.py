blocks_premise = 35.0 + 65.0 = 100.0

# the hypothesis talks about the total number of blocks in the tower, which is also mentioned in the premise
# check if the hypothesis value contradicts the estimate of blocks in the premise
if blocks_hypothesis!= blocks_premise:
    label = "contradiction"
else:
    # if the hypothesis value and estimate do not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
