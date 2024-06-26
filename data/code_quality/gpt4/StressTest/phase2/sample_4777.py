years_future_premise = 5
years_future_hypothesis = 8

# Both the premise and hypothesis talk about the age ratio of Lyn and Ele in the future
# But they refer to different points in time
if years_future_hypothesis == years_future_premise:
    # check if the hypothesis contradicts the premise by referring to the same point in time
    label = "contradiction"
else:
    # the premise and hypothesis both confirm the age ratio, but refer to different points in time
    # thus, the age ratio at the time mentioned in the hypothesis cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
