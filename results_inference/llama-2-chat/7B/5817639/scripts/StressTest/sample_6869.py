seat_bench_premise = 5
seat_bench_hypothesis = 6

# the hypothesis talks about the number of people that can be seated on a bench, referenced also in the premise
if seat_bench_hypothesis <= seat_bench_premise:
    # check if the hypothesis value contradicts the estimate of'seat_bench_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people that can be seated on a bench
    # any number of people greater than'seat_bench_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
