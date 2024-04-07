# Premise: Matt is touring a nation in which coins are issued in two amounts, 2 ¢ and 5 ¢, which are made of iron and copper, respectively.
# Hypothesis: Matt is touring a nation in which coins are issued in two amounts, more than 1 ¢ and 5 ¢, which are made of iron and copper, respectively.
# Golden Label: entailment

coin1_premise = 2
coin2_premise = 5
coin1_hypothesis = 1
coin2_hypothesis = 5

# the hypothesis refers to the types of coins mentioned in the premise
if coin1_hypothesis >= coin1_premise:
    # check if the estimate of 'coin1_hypothesis' contradicts the value of coin1 in the premise
    label = "contradiction"
elif coin2_hypothesis != coin2_premise:
    # check if the value of coin2 in the hypothesis contradicts the value of coin2 reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

