plums_premise = 12
limes_premise = 32
limes_hypothesis = 10

# the hypothesis talks about the number of limes, which is also mentioned in the premise
# compute the total number of limes in the premise
total_limes_premise = limes_premise + plums_premise

# check if the number of limes in the hypothesis contradicts the number of limes from the premise
if total_limes_hypothesis!= total_limes_premise:
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
