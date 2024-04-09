help_premise = 8
help_hypothesis = 7
earned_premise = Rs
earned_hypothesis = Rs

# the hypothesis talks about the time taken to complete the work and the amount earned, both mentioned in the premise
if help_hypothesis <= help_premise:
    # check if the hypothesis value contradicts the estimate of 'help_premise'
    label = "contradiction"
elif earned_hypothesis!= earned_premise:
    # check if the number of earned amount in the hypothesis contradicts the number of earned amount reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
