# Premise: Matt is touring a nation in which coins are issued in two amounts, 2 ¢ and 5 ¢, which are made of iron and copper, respectively.
# Hypothesis: Matt is touring a nation in which coins are issued in two amounts, less than 4 ¢ and 5 ¢, which are made of iron and copper, respectively.
# Golden Label: entailment

coin_1_premise = 2
coin_1_hypothesis = 4
coin_2_premise = 5
coin_2_hypothesis = 5

# the hypothesis talks about the coins and their amounts, referenced also in the premise
if coin_1_hypothesis <= coin_1_premise:
    # check if the hypothesis value contradicts the exact value of 'coin_1_premise'
    label = "contradiction"
elif coin_2_hypothesis != coin_2_premise:
    # check if the value of 'coin_2_hypothesis' contradicts the exact value of 'coin_2_premise'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

