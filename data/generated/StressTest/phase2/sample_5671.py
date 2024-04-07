# Premise: It takes John exactly less than 65 minutes to rake a lawn and it takes his son Todd exactly 30 minutes to rake the same lawn.
# Hypothesis: It takes John exactly 15 minutes to rake a lawn and it takes his son Todd exactly 30 minutes to rake the same lawn.
# Golden Label: neutral

john_time_premise = 65
john_time_hypothesis = 15
todd_time_premise = 30
todd_time_hypothesis = 30

# the hypothesis mentions the time taken by John and Todd to rake the lawn, referred to in the premise
if john_time_hypothesis >= john_time_premise:
    # check if the hypothesis value contradicts the estimate of less than 'john_time_premise'
    label = "contradiction"
elif todd_time_hypothesis != todd_time_premise:
    # check if the time taken by Todd in the hypothesis contradicts the time taken by Todd reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the time taken by John
    # any time less than 'john_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

