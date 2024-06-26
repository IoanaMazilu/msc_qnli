people_bench_premise = 8
people_bench_hypothesis = 6

# the hypothesis talks about the number of people to be seated on a bench, referenced also in the premise
if people_bench_hypothesis >= people_bench_premise:
    # check if the hypothesis value contradicts the estimate of less than 'people_bench_premise'
    label = "contradiction"
elif people_bench_hypothesis < people_bench_premise:
    # if the number of people in the hypothesis is less than 'people_bench_premise', we can infer entailment
    label = "entailment"

print(label)
