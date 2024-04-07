# Premise: If it takes Darcy a total of less than 80 more minutes to commute to work by walking than it takes her to commute to work by riding the train, what is the value of x?
# Hypothesis: If it takes Darcy a total of 10 more minutes to commute to work by walking than it takes her to commute to work by riding the train, what is the value of x?
# Golden Label: neutral

commute_time_diff_premise = 80
commute_time_diff_hypothesis = 10

# the hypothesis talks about the time difference of Darcy's commute to work by walking and by train, referenced also in the premise
if commute_time_diff_hypothesis >= commute_time_diff_premise:
    # check if the hypothesis value contradicts the estimate of less than 'commute_time_diff_premise'
    label = "contradiction"
elif commute_time_diff_hypothesis < commute_time_diff_premise:
    # check if the time difference in the hypothesis is less than the time difference in the premise
    label = "entailment"
else:
    # the premise gives only an estimate for the commute time difference
    # any time difference less than 'commute_time_diff_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

