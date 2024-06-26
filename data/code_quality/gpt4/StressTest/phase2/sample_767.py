father_age_future_premise = 4
father_age_future_hypothesis = 4
mother_age_past_premise = 2
mother_age_past_hypothesis = 2

# the hypothesis talks about the future age of Raj's father and the past age of Raj's mother, referenced also in the premise
if father_age_future_hypothesis >= father_age_future_premise:
    # check if the hypothesis value contradicts the estimate of 'father_age_future_premise'
    label = "contradiction"
elif mother_age_past_hypothesis != mother_age_past_premise:
    # check if the past age of Raj's mother in the hypothesis contradicts the past age of Raj's mother in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
