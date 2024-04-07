# Premise: If it takes Darcy a total of 5 more minutes to commute to work by walking than it takes her to commute to work by riding the train, what is the value of x?
# Hypothesis: If it takes Darcy a total of 3 more minutes to commute to work by walking than it takes her to commute to work by riding the train, what is the value of x?
# Golden Label: contradiction

commute_difference_premise = 5
commute_difference_hypothesis = 3

# the hypothesis refers to the difference in commuting times by walking and by train mentioned in the premise
if commute_difference_premise != commute_difference_hypothesis:
    # check if the difference in commuting times in the hypothesis contradicts the difference reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

