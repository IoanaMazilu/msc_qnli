bench_seats_premise = 6
bench_seats_hypothesis = 7
no_middle_seat_premise = 1
no_middle_seat_hypothesis = 1

# the hypothesis refers to the number of people that can be seated on the bench
if bench_seats_hypothesis <= bench_seats_premise:
    # check if the estimate of 'bench_seats_hypothesis' contradicts the number of seats reported in the premise
    label = "contradiction"
elif no_middle_seat_hypothesis!= no_middle_seat_premise:
    # check if the number of people that cannot sit on the middle seat in the hypothesis contradicts the number of people reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
