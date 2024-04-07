# Premise: In how many ways can you seat 9 people on a bench if one of them, Rohit, does not want to sit on the middle seat or at either end?
# Hypothesis: In how many ways can you seat more than 2 people on a bench if one of them, Rohit, does not want to sit on the middle seat or at either end?
# Golden Label: entailment

people_seat_premise = 9
people_seat_hypothesis = 2

# the hypothesis is referring to the number of people mentioned in the premise
if people_seat_hypothesis >= people_seat_premise:
    # check if the hypothesis value contradicts the number of people given in the premise
    label = "contradiction"
elif people_seat_hypothesis == people_seat_premise - 1:
    # check if the number of people in the hypothesis exactly matches the number of people in the premise minus 1
    label = "entailment"
else:
    # the premise gives a specific number of people
    # any number of people less than 'people_seat_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

