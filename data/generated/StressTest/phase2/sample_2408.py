# Premise: In how many ways can you seat 9 people on a bench if one of them, Rohit, does not want to sit on the middle seat or at either end?
# Hypothesis: In how many ways can you seat more than 9 people on a bench if one of them, Rohit, does not want to sit on the middle seat or at either end?
# Golden Label: contradiction

people_seat_premise = 9
people_seat_hypothesis = 9

# the hypothesis refers to the number of people who can be seated on a bench, which is also referenced in the premise
if people_seat_hypothesis < people_seat_premise:
    # check if the number of people in the hypothesis contradicts the number of people in the premise
    label = "contradiction"
elif people_seat_hypothesis == people_seat_premise:
    # check if the number of people in the hypothesis matches exactly the number of people in the premise
    label = "entailment"
else:
    # if the number of people in the hypothesis is greater than the number in the premise, it does not contradict, but it also cannot be fully entailed from the premise
    label = "neutral"

print(label)

