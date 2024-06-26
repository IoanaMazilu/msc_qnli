pilgrims_premise = 70e6
pilgrims_hypothesis = 70e6

# the hypothesis talks about the number of pilgrims to the Ganges river, which is also mentioned in the premise
if pilgrims_hypothesis!= pilgrims_premise:
    # check if the number of pilgrims in the hypothesis contradicts the number of pilgrims in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
