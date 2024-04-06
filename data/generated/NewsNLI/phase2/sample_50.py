# Premise: Woods has been been on the Ryder Cup team seven times and has a record of 13-17-2.
# Hypothesis: Tiger Woods has played in seven Ryder Cups.
# Golden Label: entailment

ryder_cup_times_premise = 7
ryder_cup_times_hypothesis = 7

# the hypothesis mentions the number of times Woods has played in the Ryder Cup, which is also mentioned in the premise
if ryder_cup_times_hypothesis != ryder_cup_times_premise:
    # check if the number of times Woods played in the Ryder Cup from the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)

