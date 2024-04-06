# Premise: There were 27.0 boys and 35.0 girls on the playground at recess and each boy went back inside paired with a girl.
# Hypothesis: 7.0 children were left on the playground now.
# Golden Label: contradiction

boys_premise = 27.0
girls_premise = 35.0
children_left_hypothesis = 7.0

# the hypothesis talks about the number of children left on the playground, which are also referenced in the premise
# compute the number of children left on the playground in the premise
children_left_premise = girls_premise - boys_premise
if children_left_hypothesis != children_left_premise:
    # check if the number of children left on the playground in the hypothesis contradicts the number of children left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

