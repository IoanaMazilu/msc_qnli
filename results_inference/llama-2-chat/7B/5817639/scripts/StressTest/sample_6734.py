route_premise = 2 nd Rd + 3 rd Ave
route_hypothesis = 5 nd Rd + 3 rd Ave

# the hypothesis refers to a different set of roads than the premise
if route_hypothesis == route_premise:
    # the hypothesis and premise refer to the same set of roads, so we can infer entailment
    label = "entailment"
else:
    # the hypothesis and premise refer to different sets of roads, so we cannot infer entailment
    label = "contradiction"

print(label)
