# Premise: From a group of 6 boys & 4 girls a Committee of 4 persons is to be formed.
# Hypothesis: From a group of 3 boys & 4 girls a Committee of 4 persons is to be formed.
# Golden Label: contradiction

boys_premise = 6
boys_hypothesis = 3
girls_premise = 4
girls_hypothesis = 4
committee_premise = 4
committee_hypothesis = 4

# the hypothesis refers to the number of boys and girls and the size of the committee mentioned in the premise
if boys_hypothesis > boys_premise:
    # check if the number of boys in the hypothesis contradicts the number of boys reported in the premise
    label = "contradiction"
elif girls_hypothesis != girls_premise:
    # check if the number of girls in the hypothesis contradicts the number of girls reported in the premise
    label = "contradiction"
elif committee_hypothesis > (boys_premise + girls_premise):
    # check if the size of the committee in the hypothesis contradicts the total number of people reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we cannot infer entailment or contradiction
    label = "neutral"

print(label)

