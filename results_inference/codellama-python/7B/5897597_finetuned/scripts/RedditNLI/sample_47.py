drains_premise = 5.12
drains_hypothesis = 1000

# the hypothesis and premise mention the amount of money drained out of the economy in the current account of Poland and Turkey in July 2017
if drains_hypothesis!= drains_premise:
    # check if the amount of money drained in the hypothesis contradicts the amount of money drained in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
