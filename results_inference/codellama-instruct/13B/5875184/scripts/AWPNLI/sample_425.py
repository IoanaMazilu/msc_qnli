bought_toys_premise = True
bought_marbles_premise = 9.05
bought_football_premise = 4.95
received_baseball_premise = 6.52

# the hypothesis refers to the net amount spent on toys, which are also mentioned in the premise
# compute the total amount spent on toys
total_toys_premise = bought_marbles_premise + bought_football_premise - received_baseball_premise
if total_toys_premise!= 3.7:
    # check if the net amount of toys in the hypothesis contradicts the total amount of toys from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
