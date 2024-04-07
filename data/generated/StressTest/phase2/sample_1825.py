# Premise: If Bill needs to walk from the corner of less than 7 nd Rd and 3 rd Ave to the corner of 6 th Rd and 9 th Ave in the shortest possible time, how many different routes could he take?
# Hypothesis: If Bill needs to walk from the corner of 2 nd Rd and 3 rd Ave to the corner of 6 th Rd and 9 th Ave in the shortest possible time, how many different routes could he take?
# Golden Label: neutral

start_road_premise = 7
start_road_hypothesis = 2
start_ave_premise = 3
start_ave_hypothesis = 3
end_road_premise = 6
end_road_hypothesis = 6
end_ave_premise = 9
end_ave_hypothesis = 9

# the hypothesis specifies a starting location that is on a lower numbered road than specified in the premise
if start_road_hypothesis >= start_road_premise:
    # check if the road number in the hypothesis contradicts the estimate of less than 'start_road_premise'
    label = "contradiction"
elif start_ave_hypothesis != start_ave_premise or end_road_hypothesis != end_road_premise or end_ave_hypothesis != end_ave_premise:
    # check if the starting avenue or ending locations in the hypothesis contradict the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the starting road
    # any road number less than 'start_road_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

