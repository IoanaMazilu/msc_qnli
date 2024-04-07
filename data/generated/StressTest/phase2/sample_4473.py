# Premise: If it takes Darcy a total of 20 more minutes to commute to work by walking than it takes her to commute to work by riding the train, what is the value of x?
# Hypothesis: If it takes Darcy a total of less than 50 more minutes to commute to work by walking than it takes her to commute to work by riding the train, what is the value of x?
# Golden Label: entailment

commute_time_diff_premise = 20
commute_time_diff_hypothesis = 50

# the hypothesis refers to the difference in commute time mentioned in the premise
if commute_time_diff_hypothesis <= commute_time_diff_premise:
    # check if the estimate of 'commute_time_diff_hypothesis' contradicts the commute time difference in the premise
    label = "contradiction"
else:
    # the hypothesis estimate for the commute time difference is larger than the premise's
    # so it does not contradict the premise, but it also cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

