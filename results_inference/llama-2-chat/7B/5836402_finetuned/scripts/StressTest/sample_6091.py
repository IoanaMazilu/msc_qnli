p_premise = 1
p_hypothesis = 2

# the hypothesis talks about the prime number p, referenced also in the premise
if p_hypothesis!= p_premise:
    # check if the value of p in the hypothesis contradicts the value of p in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
