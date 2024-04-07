# Premise: How many possible ways can 2 girls (Rebecca, Kate, Ashley) go on a date with 3 boys (Peter, Kyle, Sam)?
# Hypothesis: How many possible ways can 1 girls (Rebecca, Kate, Ashley) go on a date with 3 boys (Peter, Kyle, Sam)?
# Golden Label: contradiction

girls_premise = 2
boys_premise = 3
girls_hypothesis = 1
boys_hypothesis = 3

# the hypothesis talks about the number of girls and boys going on a date, also referred to in the premise
if girls_hypothesis != girls_premise:
    # check if the number of girls in the hypothesis contradicts the number of girls in the premise
    label = "contradiction"
elif boys_hypothesis != boys_premise:
    # check if the number of boys in the hypothesis contradicts the number of boys in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

