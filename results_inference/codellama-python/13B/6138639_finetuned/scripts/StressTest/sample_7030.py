start_road_premise = 7
start_road_hypothesis = 2
end_road_premise = 9
end_road_hypothesis = 9

# the hypothesis talks about the starting and ending roads for Bill's walk, referenced also in the premise
if start_road_hypothesis >= start_road_premise:
    # check if the hypothesis value contradicts the estimate of less than'start_road_premise'
    label = "contradiction"
elif end_road_hypothesis!= end_road_premise:
    # check if the ending road in the hypothesis contradicts the ending road reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the starting road
    # any starting road less than'start_road_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
