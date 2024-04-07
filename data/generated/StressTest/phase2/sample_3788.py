# Premise: How many possible ways can 1 girls (Rebecca, Kate, Ashley) go on a date with 3 boys (Peter, Kyle, Sam)?
# Hypothesis: How many possible ways can 5 girls (Rebecca, Kate, Ashley) go on a date with 3 boys (Peter, Kyle, Sam)?
# Golden Label: contradiction

girls_premise = 1
girls_hypothesis = 5
boys_premise = 3
boys_hypothesis = 3

# the hypothesis talks about the number of girls and boys mentioned in the premise
if boys_hypothesis != boys_premise:
    # check if the number of boys in the hypothesis contradicts the number of boys in the premise
    label = "contradiction"
elif girls_hypothesis <= girls_premise:
    # check if the number of girls in the hypothesis contradicts the number of girls in the premise
    label = "contradiction"
else:
    # the premise and the hypothesis are talking about different number of girls
    # the number of girls in the hypothesis cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

