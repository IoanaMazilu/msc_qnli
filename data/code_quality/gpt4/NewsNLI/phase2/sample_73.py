murder_counts_premise = 8
murder_counts_hypothesis = 8

# the hypothesis indicates the number of murder counts faced by Guy Heinze Jr., which is also mentioned in the premise
if murder_counts_hypothesis != murder_counts_premise:
    # check if the murder counts in the hypothesis contradicts the murder counts reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
