# Premise: How many miles from home can Aaron jog so that he spends a total of less than 4 hours jogging and walking?
# Hypothesis: How many miles from home can Aaron jog so that he spends a total of 3 hours jogging and walking?
# Golden Label: neutral

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

