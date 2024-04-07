# Premise: How many possible ways can less than 7 girls (Rebecca, Kate, Ashley) go on a date with 5 boys (Peter, Kyle, Sam)?
# Hypothesis: How many possible ways can 5 girls (Rebecca, Kate, Ashley) go on a date with 5 boys (Peter, Kyle, Sam)?
# Golden Label: neutral

girls_premise = 7
girls_hypothesis = 5

# the hypothesis refers to the number of girls going on a date with boys, mentioned in the premise
if girls_hypothesis >= girls_premise:
    # check if the number of girls in the hypothesis contradicts the premise (less than 'girls_premise' girls)
    label = "contradiction"
elif girls_hypothesis < girls_premise:
    # if the number of girls in the hypothesis is less than 'girls_premise', it is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
