jane_age_premise = 32
jane_age_hypothesis = 42
jane_baby_sitting_premise = 10
jane_baby_sitting_hypothesis = 10

# the hypothesis talks about Jane's age and baby-sitting history, referenced also in the premise
if jane_age_hypothesis <= jane_age_premise:
    # check if the hypothesis value contradicts the estimate of Jane's age in the premise
    label = "contradiction"
elif jane_baby_sitting_hypothesis!= jane_baby_sitting_premise:
    # check if the number of years since Jane stopped baby-sitting in the hypothesis contradicts the number of years reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
