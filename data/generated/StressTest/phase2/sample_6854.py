# Premise: Matt is touring a nation in which coins are issued in two amounts, 2 ¢ and 5 ¢, which are made of iron and copper, respectively.
# Hypothesis: Matt is touring a nation in which coins are issued in two amounts, more than 2 ¢ and 5 ¢, which are made of iron and copper, respectively.
# Golden Label: contradiction

coin1_premise = 2
coin1_hypothesis = 2
coin2_premise = 5
coin2_hypothesis = 5

# the hypothesis refers to the coin amounts mentioned in the premise
if coin1_hypothesis <= coin1_premise and coin2_hypothesis == coin2_premise:
    # check if the 'coin1_hypothesis' contradicts the amount of coin1 in the premise
    label = "contradiction"
elif coin1_hypothesis > coin1_premise and coin2_hypothesis == coin2_premise:
    # the premise gives an exact amount for the coins
    # any amount greater than 'coin1_premise' cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

