tickets_premise = 8
tickets_hypothesis = 8
prize_premise = 1000000
prize_hypothesis = 1000000

# the hypothesis mentions the number of tickets and their value, which are also mentioned in the premise
if tickets_hypothesis != tickets_premise:
    # check if the number of tickets in the hypothesis contradicts the number of tickets reported in the premise
    label = "contradiction"
elif prize_hypothesis != prize_premise:
    # check if the value of the prizes from the hypothesis contradicts the value of prizes in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
