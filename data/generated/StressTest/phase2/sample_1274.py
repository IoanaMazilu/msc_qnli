# Premise: Matt is touring a nation in which coins are issued in two amounts, 2 ¢ and 5 ¢, which are made of iron and copper, respectively.
# Hypothesis: Matt is touring a nation in which coins are issued in two amounts, 8 ¢ and 5 ¢, which are made of iron and copper, respectively.
# Golden Label: contradiction

coin1_premise = 2
coin2_premise = 5
coin1_hypothesis = 8
coin2_hypothesis = 5

# the hypothesis refers to the value of the coins in the same country Matt is touring
if coin1_hypothesis != coin1_premise:
    # check if the value of the first coin in the hypothesis contradicts the value of the first coin in the premise
    label = "contradiction"
elif coin2_hypothesis != coin2_premise:
    # check if the value of the second coin in the hypothesis contradicts the value of the second coin in the premise
    label = "contradiction"
else:
    # if the values of the coins in the hypothesis do not contradict the values in the premise, we can infer entailment
    label = "entailment"

print(label)

