# Premise: How many possible ways can less than 6 girls (Rebecca, Kate, Ashley) go on a date with 3 boys (Peter, Kyle, Sam)?
# Hypothesis: How many possible ways can 2 girls (Rebecca, Kate, Ashley) go on a date with 3 boys (Peter, Kyle, Sam)?
# Golden Label: neutral

girls_premise = 6
girls_hypothesis = 2
boys_premise = 3
boys_hypothesis = 3

# the hypothesis refers to the number of girls and boys mentioned in the premise
if girls_hypothesis >= girls_premise:
    # check if the number of girls in the hypothesis contradicts the estimation of less than 'girls_premise'
    label = "contradiction"
elif boys_hypothesis != boys_premise:
    # check if the number of boys in the hypothesis contradicts the number of boys in the premise
    label = "contradiction"
else:
    # the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

