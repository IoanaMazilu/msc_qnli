# Premise: Tim and Stacy need to select seats in a row of chairs that are numbered in order from less than 4 to 5.
# Hypothesis: Tim and Stacy need to select seats in a row of chairs that are numbered in order from 1 to 5.
# Golden Label: neutral

seat_start_premise = 4 
seat_end_premise = 5
seat_start_hypothesis = 1
seat_end_hypothesis = 5

# the hypothesis refers to the same range of chairs mentioned in the premise
if seat_start_hypothesis >= seat_start_premise:
    # check if the start of the range in the hypothesis contradicts the premise's start of the range
    label = "contradiction"
elif seat_end_hypothesis != seat_end_premise:
    # check if the end of the range in the hypothesis contradicts the premise's end of the range
    label = "contradiction"
else:
    # the premise gives only an estimate for the start of the range
    # this means that the hypothesis does not contradict the premise, but it cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

