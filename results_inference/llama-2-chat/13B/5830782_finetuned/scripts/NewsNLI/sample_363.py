viruses_premise = 1
viruses_hypothesis = 1

# the hypothesis mentions the number of Stuxnet viruses that were able to penetrate the facility, which is also mentioned in the premise
if viruses_hypothesis!= viruses_premise:
    # check if the number of viruses in the hypothesis contradicts the number of viruses reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
