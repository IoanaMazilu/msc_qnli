pilgrimage_premise = 70e6
pilgrimage_hypothesis = 70e6

# the hypothesis talks about the number of people participating in pilgrimage to the Ganges river, which is also mentioned in the premise
if pilgrimage_hypothesis!= pilgrimage_premise:
    # check if the number of people participating in pilgrimage in the hypothesis contradicts the number of people from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
