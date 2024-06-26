fines_min_premise = 10000
fines_max_premise = 29000000
fines_max_hypothesis = 4500000

# the hypothesis mentions the maximum amount of outstanding fines, which is also mentioned in the premise
if fines_max_hypothesis!= fines_max_premise:
    # check if the maximum fine amount in the hypothesis contradicts the maximum fine amount reported in the premise
    label = "contradiction"
else:
    # if the maximum fine amount in the hypothesis does not contradict the maximum fine amount in the premise, we can infer entailment
    label = "entailment"

print(label)
