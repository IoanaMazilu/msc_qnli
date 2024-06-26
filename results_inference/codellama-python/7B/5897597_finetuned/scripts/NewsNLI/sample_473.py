slaves_premise = 30000000
slaves_hypothesis = 30000000

# the hypothesis mentions the number of people living as slaves globally, which is also mentioned in the premise
if slaves_hypothesis!= slaves_premise:
    # check if the number of slaves in the hypothesis contradicts the number of slaves reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
