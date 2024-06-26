coin1_premise = 7
coin1_hypothesis = 2
coin2_premise = 5
coin2_hypothesis = 5

# the hypothesis talks about the value of the coins in the nation Matt is touring, which is also mentioned in the premise
if coin1_hypothesis >= coin1_premise:
    # check if the value of 'coin1_hypothesis' contradicts the premise of less than 'coin1_premise'
    label = "contradiction"
elif coin2_hypothesis != coin2_premise:
    # check if the value of 'coin2_hypothesis' contradicts the 'coin2_premise' value
    label = "contradiction"
else:
    # the hypothesis values are not contradicting the premise ones, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
