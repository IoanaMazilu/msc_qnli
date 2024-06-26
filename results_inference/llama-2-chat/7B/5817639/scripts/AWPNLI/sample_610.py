dollars_premise = 73.0
dollars_hypothesis = 128.0

# the hypothesis refers to the amount of money, which is also mentioned in the premise
# compute the total amount of money in the premise
total_dollars_premise = dollars_premise + 55.0

# check if the hypothesis value contradicts the estimate from the premise
if total_dollars_hypothesis!= total_dollars_premise:
    label = "contradiction"
else:
    # if the hypothesis value and estimate do not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
