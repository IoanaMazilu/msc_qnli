apples_premise = 2.0 + 9.0
apples_hypothesis = 11.0

# the hypothesis talks about the total number of apples picked, which is also referenced in the premise
if apples_hypothesis!= apples_premise:
    # check if the total number of apples from the hypothesis contradicts the total number of apples from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
