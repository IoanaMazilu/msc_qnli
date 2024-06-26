shirts_bought_premise = 560
shirts_bought_hypothesis = 160
rate_premise = Rs.
rate_hypothesis = Rs.

# the hypothesis refers to the number of shirts bought and the rate at which they were bought
if shirts_bought_hypothesis >= shirts_bought_premise:
    # check if the number of shirts bought in the hypothesis contradicts the estimate of less than'shirts_bought_premise'
    label = "contradiction"
elif rate_hypothesis!= rate_premise:
    # check if the rate at which the shirts were bought in the hypothesis contradicts the rate mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
