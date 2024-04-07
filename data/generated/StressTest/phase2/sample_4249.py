# Premise: If it takes Darcy a total of less than 6 more minutes to commute to work by walking than it takes her to commute to work by riding the train, what is the value of x?
# Hypothesis: If it takes Darcy a total of 2 more minutes to commute to work by walking than it takes her to commute to work by riding the train, what is the value of x?
# Golden Label: neutral

commute_time_difference_premise = 6
commute_time_difference_hypothesis = 2

# the hypothesis mentions the time difference between Darcy's commute by walking or train, as stated in the premise
if commute_time_difference_hypothesis >= commute_time_difference_premise:
    # check if the hypothesis time difference contradicts the premise of less than 'commute_time_difference_premise'
    label = "contradiction"
elif commute_time_difference_hypothesis < commute_time_difference_premise:
    # any time difference less than 'commute_time_difference_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

