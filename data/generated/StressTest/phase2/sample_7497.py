# Premise: Jane is currently 34 years old, and she stopped baby-sitting 10 years ago.
# Hypothesis: Jane is currently less than 54 years old, and she stopped baby-sitting 10 years ago.
# Golden Label: entailment

jane_age_premise = 34
jane_age_hypothesis = 54
stopped_babysitting_premise = 10
stopped_babysitting_hypothesis = 10

# the hypothesis talks about Jane's age and the time she stopped babysitting, both referenced in the premise
if jane_age_hypothesis <= jane_age_premise:
    # check if the hypothesis value contradicts the exact age of Jane in the premise
    label = "contradiction"
elif stopped_babysitting_hypothesis != stopped_babysitting_premise:
    # check if the time Jane stopped babysitting in the hypothesis contradicts the time mentioned in the premise
    label = "contradiction"
elif jane_age_hypothesis == (jane_age_premise + 20):
    # check if the hypothesis value is exactly 20 years more than the premise which would be a contradiction 
    # because Jane is not exactly 54 years old
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

