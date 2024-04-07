# Premise: How many possible ways can 1 girls (Rebecca, Kate, Ashley) go on a date with 3 boys (Peter, Kyle, Sam)?
# Hypothesis: How many possible ways can less than 7 girls (Rebecca, Kate, Ashley) go on a date with 3 boys (Peter, Kyle, Sam)?
# Golden Label: entailment

girls_premise = 1
girls_hypothesis = 7
boys_premise = 3
boys_hypothesis = 3

# the hypothesis refers to the number of possible date ways between girls and boys mentioned in the premise
if girls_hypothesis < girls_premise:
    # check if the number 'girls_hypothesis' contradicts the number of girls in the premise
    label = "contradiction"
elif boys_hypothesis != boys_premise:
    # check if the number of boys in the hypothesis contradicts the number of boys reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

