start_premise = (2, 3)
end_premise = (10, 5)
start_hypothesis = (5, 3)
end_hypothesis = (10, 5)

# the hypothesis refers to the starting and ending points of Bill's walk, which are also mentioned in the premise
if start_hypothesis!= start_premise or end_hypothesis!= end_premise:
    # check if the starting or ending points in the hypothesis contradict the ones mentioned in the premise
    label = "contradiction"
else:
    # if the starting and ending points in the hypothesis do not contradict the ones in the premise, we can infer entailment
    label = "entailment"

print(label)
