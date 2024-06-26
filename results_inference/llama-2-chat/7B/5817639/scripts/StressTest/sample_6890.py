seat_bench_premise = 6
seat_bench_hypothesis = 7

# the hypothesis talks about the number of ways to seat people on a bench, referenced also in the premise
if seat_bench_hypothesis <= seat_bench_premise:
    # check if the hypothesis value contradicts the estimate of'seat_bench_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of ways to seat people on a bench
    # any number of ways greater than'seat_bench_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
