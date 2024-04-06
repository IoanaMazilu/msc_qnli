# Premise: In the May 2005 general election Michael Howard failed to unseat the Labour Government, although the Conservatives did gain 33 seats, playing the most significant role in reducing Labour's majority from 167 to 66.
# Hypothesis: In the May 2005 general election Conservatives got 33 seats.
# Golden Label: neutral

conservatives_gain_premise = 33
conservatives_gain_hypothesis = 33

# the hypothesis talks about the number of seats gained by the Conservatives in the election, which is also mentioned in the premise
if conservatives_gain_hypothesis == conservatives_gain_premise:
    # if the number of seats gained by the Conservatives in the hypothesis is the same as in the premise, we can infer entailment
    label = "entailment"
else:
    # if the number of seats gained by the Conservatives in the hypothesis is not the same as in the premise, we have a contradiction
    label = "contradiction"

print(label)

