jogging_walking_time_premise = 4
jogging_walking_time_hypothesis = 3

# the hypothesis talks about the total time Aaron spends jogging and walking, which is also mentioned in the premise
if jogging_walking_time_hypothesis >= jogging_walking_time_premise:
    # check if the time mentioned in the hypothesis contradicts the premise
    label = "contradiction"
elif jogging_walking_time_hypothesis < jogging_walking_time_premise:
    # if the time in the hypothesis is less than the time in the premise
    # it is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
