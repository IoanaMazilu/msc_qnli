range_premise = 60
range_hypothesis = 37

# the hypothesis mentions the range of the rockets in miles, which is also mentioned in the premise
if range_hypothesis!= range_premise:
    # check if the range in the hypothesis contradicts the range reported in the premise
    label = "contradiction"
else:
    # if the range in the hypothesis does not contradict the range in the premise, we can infer entailment
    label = "entailment"

print(label)
