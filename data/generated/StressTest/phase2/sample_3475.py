# Premise: In how many ways can you seat less than 7 people on a bench if one of them, Rohit, does not want to sit on the middle seat or at either end?
# Hypothesis: In how many ways can you seat 4 people on a bench if one of them, Rohit, does not want to sit on the middle seat or at either end?
# Golden Label: neutral

people_bench_premise = 7
people_bench_hypothesis = 4

# the hypothesis asks about a specific number of people seating on a bench, which is also referenced in the premise
if people_bench_hypothesis >= people_bench_premise:
    # check if the hypothesis value contradicts the estimate of less than 'people_bench_premise'
    label = "contradiction"
elif people_bench_hypothesis < people_bench_premise:
    # the premise gives only an estimate for the number of people
    # any number of people less than 'people_bench_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis value is consistent with the premise, we can infer entailment
    label = "entailment"

print(label)

