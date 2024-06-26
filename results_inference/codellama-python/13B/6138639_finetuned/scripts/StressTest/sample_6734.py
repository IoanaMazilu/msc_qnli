start_premise = [2, 3]
end_premise = [10, 5]
start_hypothesis = [5, 3]
end_hypothesis = [10, 5]

# the hypothesis talks about the start and end points of the route, referenced also in the premise
if start_hypothesis!= start_premise or end_hypothesis!= end_premise:
    # check if the start and end points in the hypothesis contradict the start and end points in the premise
    label = "contradiction"
else:
    # the premise and hypothesis are identical in terms of start and end points
    # any route from'start_premise' to 'end_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
