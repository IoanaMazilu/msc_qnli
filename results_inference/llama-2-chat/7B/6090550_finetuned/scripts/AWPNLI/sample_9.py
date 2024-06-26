dimes_premise = 7.0 + 8.0 + 4.0
dimes_hypothesis = 18.0

# the hypothesis refers to the total number of dimes, which is also mentioned in the premise
if dimes_hypothesis!= dimes_premise:
    # check if the total number of dimes in the hypothesis contradicts the total number of dimes reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
