loneliest_road_premise = "The Loneliest Road in America"
loneliest_road_hypothesis = "Nevada stretch of U.S. Route 50 dubbed'' The Loneliest Road in America''"

# check if the hypothesis mentions the same entity as the premise
if loneliest_road_hypothesis!= loneliest_road_premise:
    # if the hypothesis and premise entities do not match, the relation is contradiction
    label = "contradiction"
else:
    # if the entities match, we can infer entailment
    label = "entailment"

print(label)
