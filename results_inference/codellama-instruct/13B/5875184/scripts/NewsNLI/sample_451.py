officials_premise = 48
officials_hypothesis = 48
primates_premise = 2
primates_hypothesis = 2

# the hypothesis mentions the number of animals killed by law enforcement and the number of primates killed by the other animals, which are also mentioned in the premise
if officials_hypothesis!= officials_premise:
    # check if the number of animals killed by law enforcement in the hypothesis contradicts the number of animals killed by law enforcement in the premise
    label = "contradiction"
elif primates_hypothesis!= primates_premise:
    # check if the number of primates killed by the other animals in the hypothesis contradicts the number of primates killed by the other animals in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
