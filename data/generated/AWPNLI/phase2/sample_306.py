# Premise: For Halloween Sarah received 108.0 pieces of candy and she ate 36.0 pieces then placed the rest into piles with 9.0 in each pile.
# Hypothesis: She could make 8.0 piles.
# Golden Label: entailment

received_candy_premise = 108.0
ate_candy_premise = 36.0
pile_size_premise = 9.0
total_piles_hypothesis = 8.0

# the hypothesis refers to the number of candy piles, which are also mentioned in the premise
# compute the total number of piles in the premise
total_piles_premise = (received_candy_premise - ate_candy_premise) / pile_size_premise
if total_piles_hypothesis != total_piles_premise:
    # check if the number of piles in the hypothesis contradicts the number of piles from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

