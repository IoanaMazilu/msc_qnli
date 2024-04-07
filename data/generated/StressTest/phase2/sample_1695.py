# Premise: Jane is currently 32 years old, and she stopped baby-sitting 10 years ago.
# Hypothesis: Jane is currently more than 12 years old, and she stopped baby-sitting 10 years ago.
# Golden Label: entailment

jane_age_premise = 32
jane_age_hypothesis = 12
babysitting_stop_premise = 10
babysitting_stop_hypothesis = 10

# the hypothesis talks about Jane's age and when she stopped babysitting, both also mentioned in the premise
if jane_age_premise <= jane_age_hypothesis:
    # check if the hypothesis value contradicts the mentioned age of Jane in the premise
    label = "contradiction"
elif babysitting_stop_premise != babysitting_stop_hypothesis:
    # check if the time mentioned for stopping babysitting contradicts the one mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

