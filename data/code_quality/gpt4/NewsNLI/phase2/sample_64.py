murder_counts_premise = 6
murder_counts_hypothesis = 1

# the hypothesis mentions that Mesac Damas is charged with a first-degree murder, which is also mentioned in the premise
# however, the premise mentions six counts of first-degree murder, while the hypothesis mentions only one count
if murder_counts_premise != murder_counts_hypothesis:
    # check if the number of murder counts in the hypothesis contradicts the number of murder counts in the premise
    label = "contradiction"
else:
    # if the number of murder counts in the hypothesis does not contradict the number of murder counts in the premise,
    # we can infer entailment
    label = "neutral"

print(label)
