raises_premise = 1
raises_hypothesis = 1

# the hypothesis and premise mention the number of rate hikes in 2018
if raises_premise!= raises_hypothesis:
    # check if the number of rate hikes in the hypothesis contradicts the number of rate hikes in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
