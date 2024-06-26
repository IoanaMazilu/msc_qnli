tshirts_bought_premise = 8
tshirts_bought_hypothesis = 8

# the hypothesis talks about the number of t-shirts bought by Sanoop, which is also mentioned in the premise
if tshirts_bought_hypothesis!= tshirts_bought_premise:
    # check if the number of t-shirts bought in the hypothesis contradicts the number of t-shirts bought in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
