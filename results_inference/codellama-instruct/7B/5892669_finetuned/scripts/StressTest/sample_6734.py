start_premise = (2, 3)
end_premise = (10, 5)
start_hypothesis = (5, 3)
end_hypothesis = (10, 5)

# the hypothesis refers to the starting and ending points of Bill's walk mentioned in the premise
if start_premise!= start_hypothesis or end_premise!= end_hypothesis:
    # check if the starting or ending points in the hypothesis contradict the ones in the premise
    label = "contradiction"
else:
    # if the starting and ending points in the hypothesis do not contradict the ones in the premise, we can infer entailment
    label = "entailment"

print(label)
