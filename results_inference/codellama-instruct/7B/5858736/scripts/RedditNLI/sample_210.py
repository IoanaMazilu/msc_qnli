rate_premise = 2
rate_hypothesis = 2

# the hypothesis and premise mention the number of rate hikes in 2018
if rate_hypothesis!= rate_premise:
    # check if the number of rate hikes in the hypothesis contradicts the number of rate hikes in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)