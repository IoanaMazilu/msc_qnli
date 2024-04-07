# Premise: In a group of 6 boys & 4 girls a Committee of 4 persons is to be formed.
# Hypothesis: In a group of 4 boys & 4 girls a Committee of 4 persons is to be formed.
# Golden Label: contradiction

boys_premise = 6
girls_premise = 4
boys_hypothesis = 4
girls_hypothesis = 4

# the hypothesis refers to the number of boys and girls in a group, which is also mentioned in the premise
if boys_hypothesis > boys_premise or girls_hypothesis > girls_premise:
    # check if the number of boys or girls in the hypothesis contradicts the number of boys or girls mentioned in the premise
    label = "contradiction"
elif boys_hypothesis == boys_premise and girls_hypothesis == girls_premise:
    # check if the number of boys and girls in the hypothesis is exactly the same as in the premise
    label = "entailment"
else:
    # the number of boys and girls in the hypothesis does not contradict the premise, but cannot be fully entailed from the premise either
    label = "neutral"

print(label)

