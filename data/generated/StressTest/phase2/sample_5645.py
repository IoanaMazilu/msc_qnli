# Premise: Matt is touring a nation in which coins are issued in two amounts, 2 ¢ and 5 ¢, which are made of iron and copper, respectively.
# Hypothesis: Matt is touring a nation in which coins are issued in two amounts, 5 ¢ and 5 ¢, which are made of iron and copper, respectively.
# Golden Label: contradiction

coin1_premise = 2
coin2_premise = 5
coin1_hypothesis = 5
coin2_hypothesis = 5

# the hypothesis refers to the amounts of the two types of coins in the nation Matt is visiting, which are also mentioned in the premise
if coin1_hypothesis != coin1_premise:
    # check if the amount of the first type of coin in the hypothesis contradicts the amount of the first type of coin in the premise
    label = "contradiction"
elif coin2_hypothesis != coin2_premise:
    # check if the amount of the second type of coin in the hypothesis contradicts the amount of the second type of coin in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

