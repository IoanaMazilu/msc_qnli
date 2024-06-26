sale_premise = 27.5e9
sale_hypothesis = 27.5e9

# the hypothesis talks about the total cost of the sale, which is also mentioned in the premise
if sale_hypothesis!= sale_premise:
    # check if the total cost in the hypothesis contradicts the total cost from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
