# Premise: Tim and Stacy need to select seats in a row of chairs that are numbered in order from 1 to 5.
# Hypothesis: Tim and Stacy need to select seats in a row of chairs that are numbered in order from less than 4 to 5.
# Golden Label: entailment

seat_numbers_premise = 5
seat_numbers_hypothesis = 4

# the hypothesis talks about the number of seats available, referenced also in the premise
if seat_numbers_hypothesis >= seat_numbers_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
elif seat_numbers_hypothesis < seat_numbers_premise:
    # the premise gives the total number of seats and the hypothesis gives lesser number, but doesn't explicitly contradict the premise
    label = "neutral"

print(label)

