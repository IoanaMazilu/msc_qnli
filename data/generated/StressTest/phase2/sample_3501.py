# Premise: In a group of 6 boys & 4 girls a Committee of 4 persons is to be formed.
# Hypothesis: In a group of less than 8 boys & 4 girls a Committee of 4 persons is to be formed.
# Golden Label: entailment

boys_group_premise = 6
boys_group_hypothesis = 8
girls_group_premise = 4
girls_group_hypothesis = 4
committee_size_premise = 4
committee_size_hypothesis = 4

# the hypothesis talks about the number of boys and girls in a group and the committee size, referenced also in the premise
if boys_group_premise >= boys_group_hypothesis:
    # check if the number of boys in the premise contradicts the number of boys in the hypothesis
    label = "contradiction"
elif girls_group_premise != girls_group_hypothesis or committee_size_premise != committee_size_hypothesis:
    # check if the number of girls or the committee size in the premise contradicts the number of girls or the committee size in the hypothesis
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

