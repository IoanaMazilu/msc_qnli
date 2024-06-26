people_between_premise = 7
people_between_hypothesis = 8
people_after_premise = 20
people_after_hypothesis = 20

# the hypothesis talks about the number of people entering the theater, similar to the premise
if people_between_hypothesis != people_between_premise:
    # check if the number of people between in the hypothesis contradicts the number of people between in the premise
    label = "contradiction"
elif people_after_hypothesis != people_after_premise:
    # check if the number of people after in the hypothesis contradicts the number of people after in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
