boys_premise = 6
boys_hypothesis = 3
girls_premise = 4
girls_hypothesis = 4
committee_premise = 4
committee_hypothesis = 4

# the hypothesis refers to the number of boys and girls in a group and the committee to be formed, all mentioned in the premise
if boys_hypothesis > boys_premise or girls_hypothesis!= girls_premise:
    # check if the number of boys or girls in the hypothesis contradicts the number of boys or girls in the premise
    label = "contradiction"
elif committee_hypothesis!= committee_premise:
    # check if the number of committee members in the hypothesis contradicts the number of committee members in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
# 