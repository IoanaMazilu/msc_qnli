father_age_premise = 38
father_age_hypothesis = 18
mother_age_premise = 36
mother_age_hypothesis = 36

# the hypothesis talks about the age of Ayesha's father and mother when she was born and her brother was born
if father_age_hypothesis == father_age_premise and mother_age_hypothesis == mother_age_premise:
    # check if the hypothesis values match the premise values
    label = "entailment"
else:
    # if the hypothesis values contradict the premise values, we can infer contradiction
    label = "contradiction"

print(label)
