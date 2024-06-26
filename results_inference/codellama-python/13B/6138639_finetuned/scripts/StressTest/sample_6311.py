boys_premise = 6
boys_hypothesis = 1
girls_premise = 4
girls_hypothesis = 4
committee_size_premise = 4
committee_size_hypothesis = 4

# the hypothesis talks about the number of boys and girls in a group, referenced also in the premise
if boys_hypothesis > boys_premise or girls_hypothesis!= girls_premise:
    # check if the hypothesis values contradict the premise ones
    label = "contradiction"
elif committee_size_hypothesis!= committee_size_premise:
    # check if the committee size in the hypothesis contradicts the committee size reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
