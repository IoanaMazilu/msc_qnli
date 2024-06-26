received_candy_premise = 108.0
ate_candy_premise = 36.0
pile_size_premise = 9.0
piles_hypothesis = 4.0

# the hypothesis refers to the number of piles, which are also mentioned in the premise
# compute the number of piles in the premise
piles_premise = received_candy_premise / pile_size_premise
if piles_hypothesis!= piles_premise:
    # check if the number of piles in the hypothesis contradicts the number of piles from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
