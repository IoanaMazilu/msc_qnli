# Premise: From a group of 6 boys & 4 girls a Committee of 4 persons is to be formed.
# Hypothesis: From a group of more than 1 boys & 4 girls a Committee of 4 persons is to be formed.
# Golden Label: entailment

boys_premise = 6
boys_hypothesis = 1
girls_premise = 4
girls_hypothesis = 4
committee_premise = 4
committee_hypothesis = 4

# the hypothesis talks about the number of boys and girls in a group and the committee size, referenced also in the premise
if boys_hypothesis > boys_premise:
    # check if the hypothesis value contradicts the number of boys in the premise
    label = "contradiction"
elif girls_hypothesis != girls_premise:
    # check if the number of girls in the hypothesis contradicts the number of girls in the premise
    label = "contradiction"
elif committee_hypothesis != committee_premise:
    # check if the committee size in the hypothesis contradicts the committee size in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

