arrests_premise = 8
arrests_hypothesis = 8

# the hypothesis mentions the number of arrests and the lack of serious injuries reported, which are also mentioned in the premise
if arrests_hypothesis != arrests_premise:
    # check if the number of arrests in the hypothesis contradicts the number of arrests reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
