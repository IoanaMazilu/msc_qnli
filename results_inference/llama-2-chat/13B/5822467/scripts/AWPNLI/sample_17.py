pears_premise = 46.0 + 47.0 + 12.0  # compute the total number of pears picked in the premise
hypothesis_pears = 101.0

# check if the number of pears in the hypothesis contradicts the number of pears from the premise
if hypothesis_pears!= pears_premise:
    label = "contradiction"
elif hypothesis_pears > pears_premise:
    # check if the number of pears in the hypothesis entails the estimate of more than 'pears_premise'
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
