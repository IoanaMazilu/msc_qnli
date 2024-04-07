# Premise: From a group of 6 boys & 4 girls a Committee of 4 persons is to be formed.
# Hypothesis: From a group of more than 2 boys & 4 girls a Committee of 4 persons is to be formed.
# Golden Label: entailment

boys_group_premise = 6
boys_group_hypothesis = 2
girls_group_premise = 4
girls_group_hypothesis = 4
committee_premise = 4
committee_hypothesis = 4

# the hypothesis refers to the number of boys and girls in a group and the number of persons in a committee, mentioned in the premise
if boys_group_hypothesis >= boys_group_premise:
    # check if the estimate of 'boys_group_hypothesis' contradicts the number of boys in the group in the premise
    label = "contradiction"
elif girls_group_hypothesis != girls_group_premise or committee_hypothesis != committee_premise:
    # check if the number of girls in the group or the number of persons in the committee in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

