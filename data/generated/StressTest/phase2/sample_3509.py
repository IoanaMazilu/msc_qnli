# Premise: Matt is touring a nation in which coins are issued in two amounts, 2 ¢ and 5 ¢, which are made of iron and copper, respectively.
# Hypothesis: Matt is touring a nation in which coins are issued in two amounts, less than 2 ¢ and 5 ¢, which are made of iron and copper, respectively.
# Golden Label: contradiction

coin1_value_premise = 2
coin2_value_premise = 5
coin1_value_hypothesis = 2
coin2_value_hypothesis = 5

# the hypothesis talks about the value of two types of coins in a country, which is also mentioned in the premise
if coin1_value_hypothesis >= coin1_value_premise:
    # check if the value of the first coin in the hypothesis contradicts the value of the first coin in the premise
    label = "contradiction"
elif coin2_value_hypothesis != coin2_value_premise:
    # check if the value of the second coin in the hypothesis contradicts the value of the second coin in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

