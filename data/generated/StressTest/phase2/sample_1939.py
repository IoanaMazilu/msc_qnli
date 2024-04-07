# Premise: It takes John exactly less than 60 minutes to rake a lawn and it takes his son Todd exactly 60 minutes to rake the same lawn.
# Hypothesis: It takes John exactly 30 minutes to rake a lawn and it takes his son Todd exactly 60 minutes to rake the same lawn.
# Golden Label: neutral

john_time_premise = 60
john_time_hypothesis = 30
todd_time_premise = 60
todd_time_hypothesis = 60

# the hypothesis talks about the time John and Todd take to rake a lawn, which is referenced also in the premise
if john_time_hypothesis >= john_time_premise:
    # check if the hypothesis value contradicts the estimate of less than 'john_time_premise'
    label = "contradiction"
elif todd_time_hypothesis != todd_time_premise:
    # check if the time Todd takes in the hypothesis contradicts the time Todd takes reported in the premise
    label = "contradiction"
else:
    # the premise gives exactly the time for Todd and an estimate for John
    # any time less than 'john_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

