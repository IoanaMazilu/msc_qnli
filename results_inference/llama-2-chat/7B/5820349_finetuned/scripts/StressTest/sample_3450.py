join_time_premise = 2
join_time_hypothesis = 8

# the hypothesis refers to the time when Jose joined, which is also mentioned in the premise
if join_time_premise > join_time_hypothesis:
    # check if the time in the premise contradicts the estimate of 'join_time_hypothesis'
    label = "contradiction"
elif join_time_premise < join_time_hypothesis:
    # if the time in the premise is less than the estimate in the hypothesis, we can infer entailment
    label = "entailment"
else:
    # if the time in the premise matches the estimate in the hypothesis, we can infer neutrality
    label = "neutral"

print(label)
