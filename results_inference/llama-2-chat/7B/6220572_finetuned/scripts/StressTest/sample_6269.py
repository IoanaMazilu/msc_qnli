death_premise = 10
death_hypothesis = 10
flee_premise = 20
flee_hypothesis = 20

# the hypothesis refers to the number of people who died and the number of people who fled the village mentioned in the premise
if death_hypothesis >= death_premise:
    # check if the estimate of 'death_hypothesis' contradicts the number of people who died in the premise
    label = "contradiction"
elif flee_hypothesis!= flee_premise:
    # check if the number of people who fled in the hypothesis contradicts the number of people who fled reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
