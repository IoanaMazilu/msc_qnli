# Premise: If Bill needs to walk from the corner of 2 nd Rd and 3 rd Ave to the corner of 7 th Rd and 8 th Ave in the shortest possible time, how many different routes could he take?
# Hypothesis: If Bill needs to walk from the corner of more than 1 nd Rd and 3 rd Ave to the corner of 7 th Rd and 8 th Ave in the shortest possible time, how many different routes could he take?
# Golden Label: entailment

start_road_premise = 2
start_road_hypothesis = 1

# the hypothesis refers to the start and end points of Bill's walk, which are also mentioned in the premise
if start_road_hypothesis >= start_road_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

