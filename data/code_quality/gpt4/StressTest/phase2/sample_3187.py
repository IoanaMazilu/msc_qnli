ratio_premise = 8/3  # In premise Arun's age to Deepak's age is less than 8:3
ratio_hypothesis = 4/3  # In hypothesis Arun's age to Deepak's age is 4:3

# the hypothesis talks about the age ratio between Arun and Deepak, referenced also in the premise
if ratio_hypothesis >= ratio_premise:
    # check if the age ratio in the hypothesis contradicts the estimate of less than 'ratio_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the age ratio
    # any age ratio less than 'ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
