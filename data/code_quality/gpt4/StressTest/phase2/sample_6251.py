boys_premise = 6
boys_hypothesis = 6
girls_premise = 4
girls_hypothesis = 4
committee_size_premise = 4
committee_size_hypothesis = 4

# the hypothesis refers to the number of boys and girls in a group and the committee size, mentioned also in the premise
if boys_hypothesis != boys_premise:
    # check if the number of boys in the hypothesis contradicts the number of boys reported in the premise
    label = "contradiction"
elif girls_hypothesis != girls_premise or committee_size_hypothesis != committee_size_premise:
    # check if the number of girls or the committee size in the hypothesis contradicts the respective numbers in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
