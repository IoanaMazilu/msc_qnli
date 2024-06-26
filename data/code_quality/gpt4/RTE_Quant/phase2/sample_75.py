citizens_premise = 360e6
citizens_hypothesis = 360e6

# the hypothesis talks about the number of European citizens, which is also mentioned in the premise
if citizens_hypothesis != citizens_premise:
    # check if the number of European citizens in the hypothesis contradicts the number of European citizens from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
