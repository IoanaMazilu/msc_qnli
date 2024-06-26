senior_md_premise = 5
md_premise = 6
senior_md_hypothesis = 6
md_hypothesis = 6

# the hypothesis talks about the number of Senior Managing Directors and Managing Directors in Goldman Limited
if senior_md_hypothesis <= senior_md_premise:
    # check if the hypothesis estimate contradicts the exact number of Senior Managing Directors in the premise
    label = "contradiction"
elif md_hypothesis != md_premise:
    # check if the number of Managing Directors in the hypothesis contradicts the exact number of Managing Directors in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
