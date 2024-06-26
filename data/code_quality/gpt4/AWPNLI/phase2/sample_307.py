received_candy_premise = 108.0
ate_candy_premise = 36.0
pile_candy_premise = 9.0
pile_candy_hypothesis = 4.0

# the hypothesis is about the number of piles that can be made, which is also discussed in the premise
# compute the number of candies left and the number of piles that can be made from the premise
remaining_candy_premise = received_candy_premise - ate_candy_premise
pile_from_premise = remaining_candy_premise / pile_candy_premise

if pile_candy_hypothesis != pile_from_premise:
    # check if the number of piles in the hypothesis contradicts the number of piles from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
