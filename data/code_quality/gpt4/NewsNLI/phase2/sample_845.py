points_premise = 15
points_hypothesis = None # No points mentioned in the hypothesis
group_premise = 'E'
group_hypothesis = 'H'
win_premise = 3-0
win_hypothesis = 2-0

# The hypothesis mentions a different group, Group H, and a different team, Shakhtar Donetsk, claiming the top spot.
# The premise mentions Group E, in which Bayern Munich finishes top with 15 points.
# The hypothesis does not mention the points with which Shakhtar Donetsk claims the top spot.
# Therefore, no comparison can be made between the two sentences in terms of points.

if group_premise != group_hypothesis:
    # Check if the group in the hypothesis contradicts the group in the premise
    label = "neutral"

print(label)
