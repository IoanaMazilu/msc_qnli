# Premise: A train leaves Delhi at 9 a.
# Hypothesis: A train leaves Delhi at less than 9 a.
# Golden Label: contradiction

departure_time_premise = 9
departure_time_hypothesis = 9

# the hypothesis refers to the train departure time mentioned in the premise
if departure_time_hypothesis >= departure_time_premise:
    # check if the departure time in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the departure time in hypothesis is less than the premise, it cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

