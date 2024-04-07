# Premise: If it takes Darcy a total of less than 50 more minutes to commute to work by walking than it takes her to commute to work by riding the train, what is the value of x?
# Hypothesis: If it takes Darcy a total of 20 more minutes to commute to work by walking than it takes her to commute to work by riding the train, what is the value of x?
# Golden Label: neutral

commute_difference_premise = 50
commute_difference_hypothesis = 20

# the hypothesis talks about the difference in commuting time by walking and by train, referenced also in the premise
if commute_difference_hypothesis >= commute_difference_premise:
    # check if the hypothesis value contradicts the premise estimate of less than 'commute_difference_premise'
    label = "contradiction"
elif commute_difference_hypothesis < commute_difference_premise:
    # if the hypothesis value is less than the premise estimate, it does not contradict the premise
    # but it cannot be explicitly entailed from the premise either
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
