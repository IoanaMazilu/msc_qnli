bonds_purchased_premise = 4000
bonds_purchased_hypothesis = 5000

# the hypothesis refers to the amount of US saving bonds purchased by Robert, mentioned in the premise
if bonds_purchased_hypothesis!= bonds_purchased_premise:
    # check if the amount of bonds purchased in the hypothesis contradicts the amount of bonds purchased reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
