# Premise: From a group of 6 boys & 4 girls a Committee of 4 persons is to be formed.
# Hypothesis: From a group of 1 boys & 4 girls a Committee of 4 persons is to be formed.
# Golden Label: contradiction

boys_premise = 6
boys_hypothesis = 1
girls_premise = 4
girls_hypothesis = 4
committee_premise = 4
committee_hypothesis = 4

# The hypothesis refers to the number of boys, girls, and committee members mentioned in the premise
if boys_hypothesis > boys_premise:
    # Check if the number of boys in the hypothesis contradicts the number of boys reported in the premise
    label = "contradiction"
elif girls_hypothesis != girls_premise:
    # Check if the number of girls in the hypothesis contradicts the number of girls reported in the premise
    label = "contradiction"
elif committee_hypothesis != committee_premise:
    # Check if the number of committee members in the hypothesis contradicts the number of committee members reported in the premise
    label = "contradiction"
else:
    # If the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

