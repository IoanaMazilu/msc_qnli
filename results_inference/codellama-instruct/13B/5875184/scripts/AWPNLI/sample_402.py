premise_pears = 42.0
hypothesis_pears = 25.0

# the hypothesis refers to the number of pears left, which are also mentioned in the premise
# compute the total number of pears in the premise
total_pears_premise = premise_pears - hypothesis_pears
if total_pears_premise < 0:
    # check if the number of pears in the hypothesis contradicts the number of pears from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
