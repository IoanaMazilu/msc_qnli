priests_murdered_premise = 6
priests_murdered_hypothesis = 6

# the hypothesis talks about the number of priests Cristiani is accused of murdering
# the premise also mentions the same number of priests being murdered and Cristiani's involvement
# we compare the number of priests from the hypothesis and premise
if priests_murdered_hypothesis != priests_murdered_premise:
    # check if the number of priests murdered in the hypothesis contradicts the number of priests murdered in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
