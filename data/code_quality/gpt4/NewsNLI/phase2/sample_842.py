tours_premise = 2
tours_hypothesis = 2

# the hypothesis mentions the number of tours in Iraq by Quinones, which is also mentioned in the premise
if tours_hypothesis != tours_premise:
    # check if the number of tours in the hypothesis contradicts the number of tours mentioned in the premise
    label = "contradiction"
else:
    # if the number of tours in the hypothesis does not contradict the number of tours in the premise, we can infer entailment
    label = "entailment"

print(label)
