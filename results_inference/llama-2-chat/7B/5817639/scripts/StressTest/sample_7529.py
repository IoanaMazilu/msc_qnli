boys_premise = 6
girls_premise = 4
committee_size_premise = 4
hypothesis_boys = 3
hypothesis_girls = 4

# the hypothesis talks about the gender composition of the committee, which is also referenced in the premise
if hypothesis_boys <= boys_premise:
    # check if the number of boys in the hypothesis contradicts the number of boys in the premise
    label = "contradiction"
elif hypothesis_girls!= girls_premise:
    # check if the number of girls in the hypothesis contradicts the number of girls in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
