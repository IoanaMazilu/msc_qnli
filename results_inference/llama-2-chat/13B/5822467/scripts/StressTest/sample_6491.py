borrowed_premise = 6500
borrowed_hypothesis = 1500

# the hypothesis refers to the amount of money borrowed for college education
if borrowed_hypothesis <= borrowed_premise:
    # check if the hypothesis value contradicts the estimate of 'borrowed_premise'
    label = "contradiction"
elif borrowed_premise!= borrowed_hypothesis:
    # check if the amount of money borrowed in the hypothesis contradicts the amount reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
