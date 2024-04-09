seat_count_premise = 7
seat_count_hypothesis = 6

# the hypothesis talks about the number of people that can be seated on a bench, referenced also in the premise
if seat_count_hypothesis <= seat_count_premise:
    # check if the hypothesis value contradicts the estimate of more than'seat_count_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people that can be seated on a bench
    # any number of people that can be seated on a bench greater than'seat_count_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
