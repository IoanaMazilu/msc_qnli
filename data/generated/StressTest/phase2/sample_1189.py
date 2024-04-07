# Premise: If Bill needs to walk from the corner of less than 3 nd Rd and 3 rd Ave to the corner of 8 th Rd and 7 th Ave in the shortest possible time, how many different routes could he take?
# Hypothesis: If Bill needs to walk from the corner of 2 nd Rd and 3 rd Ave to the corner of 8 th Rd and 7 th Ave in the shortest possible time, how many different routes could he take?
# Golden Label: neutral

start_road_premise = 3
start_road_hypothesis = 2

# the hypothesis talks about the starting point of Bill's journey, referenced also in the premise
if start_road_hypothesis >= start_road_premise:
    # check if the hypothesis value contradicts the estimate of less than 'start_road_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the starting point
    # any starting point less than 'start_road_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

