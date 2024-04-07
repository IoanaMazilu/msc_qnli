# Premise: In how many ways can you seat 4 people on a bench if one of them, Rohit, does not want to sit on the middle seat or at either end?
# Hypothesis: In how many ways can you seat more than 1 people on a bench if one of them, Rohit, does not want to sit on the middle seat or at either end?
# Golden Label: entailment

people_seat_premise = 4
people_seat_hypothesis = 1

# the hypothesis refers to the number of people that can be seated on a bench mentioned in the premise
if people_seat_premise <= people_seat_hypothesis:
    # check if the number of 'people_seat_hypothesis' contradicts the number of people in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

