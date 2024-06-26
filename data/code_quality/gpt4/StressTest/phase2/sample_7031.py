start_premise = (2, 3)
end_premise = (9, 6)

start_hypothesis = (2, 3)
end_hypothesis = (9, 6)

# the hypothesis refers to the start and end points of Bill's journey mentioned in the premise
if start_hypothesis[0] <= start_premise[0] and start_hypothesis[1] <= start_premise[1]:
    # check if the start point in the hypothesis contradicts the start point in the premise
    label = "contradiction"
elif end_hypothesis[0] != end_premise[0] or end_hypothesis[1] != end_premise[1]:
    # check if the end point in the hypothesis contradicts the end point in the premise
    label = "contradiction"
else:
    # if the start and end points in the hypothesis do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
