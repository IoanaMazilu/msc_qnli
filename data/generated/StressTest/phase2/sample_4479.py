# Premise: How many possible ways can 3 girls (Rebecca, Kate, Ashley) go on a date with 3 boys (Peter, Kyle, Sam)?
# Hypothesis: How many possible ways can less than 6 girls (Rebecca, Kate, Ashley) go on a date with 3 boys (Peter, Kyle, Sam)?
# Golden Label: entailment

girls_premise = 3
girls_hypothesis = 6
boys_premise = 3
boys_hypothesis = 3

# the hypothesis talks about the number of girls and boys, referenced also in the premise
if boys_premise != boys_hypothesis:
    # check if the number of boys in the hypothesis contradicts the number of boys reported in the premise
    label = "contradiction"
elif girls_premise > girls_hypothesis:
    # check if the number of girls in the premise contradicts the estimate of less than 'girls_hypothesis'
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

