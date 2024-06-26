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
