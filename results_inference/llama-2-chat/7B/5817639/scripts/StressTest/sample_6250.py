boys_premise = 5
girls_premise = 4
committee_hypothesis = 6
boys_hypothesis = 6
girls_hypothesis = 4

# the hypothesis talks about the gender distribution of the group, referenced also in the premise
if committee_hypothesis <= (boys_hypothesis + girls_hypothesis):
    # check if the hypothesis value contradicts the estimate of the total number of boys and girls in the premise
    label = "contradiction"
elif boys_hypothesis!= boys_premise or girls_hypothesis!= girls_premise:
    # check if the number of boys or girls in the hypothesis contradicts the number of boys or girls reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
