# Premise: How many possible ways can less than 6 girls (Rebecca, Kate, Ashley) go on a date with 3 boys (Peter, Kyle, Sam)?
# Hypothesis: How many possible ways can 3 girls (Rebecca, Kate, Ashley) go on a date with 3 boys (Peter, Kyle, Sam)?
# Golden Label: neutral

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

