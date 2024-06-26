join_time_premise = 2
join_time_hypothesis = 8

# the hypothesis refers to the time when Jose joined, which is also mentioned in the premise
if join_time_hypothesis < join_time_premise:
    # check if the hypothesis value contradicts the exact time 'join_time_premise'
    label = "contradiction"
elif join_time_hypothesis == join_time_premise:
    # check if the hypothesis value is equal to the exact time 'join_time_premise'
    label = "entailment"
else:
    # if the hypothesis value is greater than the exact time 'join_time_premise', we can infer neutrality
    label = "neutral"

print(label)
