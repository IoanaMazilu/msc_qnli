poverty_premise = 0.045
poverty_hypothesis = 0.045

# the hypothesis mentions the number of people living in poverty in the U.S., which is also mentioned in the premise
if poverty_hypothesis!= poverty_premise:
    # check if the poverty rate in the hypothesis contradicts the poverty rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
