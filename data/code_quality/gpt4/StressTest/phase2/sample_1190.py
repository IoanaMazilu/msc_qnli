# define the starting and ending points for Bill's route in the premise and hypothesis
start_road_premise = 2
start_ave_premise = 3
end_road_premise = 8
end_ave_premise = 7

start_road_hypothesis = 8
start_ave_hypothesis = 3
end_road_hypothesis = 8
end_ave_hypothesis = 7

# The hypothesis is talking about a different starting point for the route compared to the premise 
# (different road, same avenue), but the same endpoint. 

# there is no explicit numerical information to compare, but we can compare the routes

# check if the starting and ending points in the hypothesis contradict the ones in the premise
if start_road_hypothesis != start_road_premise or start_ave_hypothesis != start_ave_premise or \
   end_road_hypothesis != end_road_premise or end_ave_hypothesis != end_ave_premise:
    label = "neutral"
else:
    label = "entailment"

print(label)
