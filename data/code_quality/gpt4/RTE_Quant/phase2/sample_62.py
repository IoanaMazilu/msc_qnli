wonders_premise = 7
wonders_hypothesis = 7

# the hypothesis talks about the lighthouse of Alexandria being one of the seven wonders, which is also mentioned in the premise
if wonders_hypothesis != wonders_premise:
    # check if the number of wonders in the hypothesis contradicts the one in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
