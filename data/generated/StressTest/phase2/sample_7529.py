# Premise: In a group of 6 boys & 4 girls a Committee of 4 persons is to be formed.
# Hypothesis: In a group of 3 boys & 4 girls a Committee of 4 persons is to be formed.
# Golden Label: contradiction

boys_premise = 6
girls_premise = 4
committee_premise = 4

boys_hypothesis = 3
girls_hypothesis = 4
committee_hypothesis = 4

# the hypothesis refers to the number of boys, girls and committee members mentioned in the premise
if boys_hypothesis > boys_premise or girls_hypothesis > girls_premise:
    # check if the number of boys or girls in the hypothesis contradicts the number in the premise
    label = "contradiction"
elif committee_hypothesis != committee_premise:
    # check if the number of committee members in the hypothesis contradicts the number in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

