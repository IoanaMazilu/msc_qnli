boys_premise = 6
girls_premise = 4
committee_size_premise = 4

# the hypothesis refers to the number of boys and girls in the premise, as well as the size of the committee
if committee_size_hypothesis <= committee_size_premise:
    # check if the estimate of 'committee_size_hypothesis' contradicts the number of committee members in the premise
    label = "contradiction"
elif boys_hypothesis >= boys_premise or girls_hypothesis >= girls_premise:
    # check if the number of boys or girls in the hypothesis contradicts the number of boys or girls reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
