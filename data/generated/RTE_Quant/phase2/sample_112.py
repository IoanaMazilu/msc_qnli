# Premise: A bus collision with a truck in Uganda has resulted in at least 30 fatalities and has left a further 21 injured.
# Hypothesis: 30 die in a bus collision in Uganda.
# Golden Label: entailment

fatalities_premise = 30
fatalities_hypothesis = 30

# the hypothesis talks about the number of fatalities from a bus collision in Uganda, which is also mentioned in the premise
if fatalities_hypothesis != fatalities_premise:
    # check if the number of fatalities in the hypothesis contradicts the number in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

