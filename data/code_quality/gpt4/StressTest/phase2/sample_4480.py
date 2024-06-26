girls_premise = 6
girls_hypothesis = 3

# the hypothesis refers to the number of girls mentioned in the premise
if girls_hypothesis >= girls_premise:
    # check if the number of girls in the hypothesis contradicts the estimate of less than 'girls_premise'
    label = "contradiction"
elif girls_hypothesis < girls_premise:
    # if the number of girls in the hypothesis is less than 'girls_premise', we can infer entailment
    label = "entailment"

print(label)
