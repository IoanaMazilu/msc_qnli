start_road_premise = 3
start_road_hypothesis = 2
start_ave_premise = 3
start_ave_hypothesis = 3
end_road_premise = 10
end_road_hypothesis = 10
end_ave_premise = 5
end_ave_hypothesis = 5

# the hypothesis refers to the starting and ending points of Bill's walk, mentioned in the premise
if start_road_hypothesis >= start_road_premise:
    # check if the hypothesis value contradicts the estimate of less than'start_road_premise'
    label = "contradiction"
elif start_ave_hypothesis!= start_ave_premise:
    # check if the starting avenue in the hypothesis contradicts the starting avenue reported in the premise
    label = "contradiction"
elif end_road_hypothesis!= end_road_premise:
    # check if the ending road in the hypothesis contradicts the ending road reported in the premise
    label = "contradiction"
elif end_ave_hypothesis!= end_ave_premise:
    # check if the ending avenue in the hypothesis contradicts the ending avenue reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the starting road
    # any road less than'start_road_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
