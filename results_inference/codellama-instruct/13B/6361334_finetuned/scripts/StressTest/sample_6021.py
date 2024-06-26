borrowed_premise = 5000
borrowed_hypothesis = 2000

# the hypothesis refers to the amount borrowed annually for college education, which is also mentioned in the premise
if borrowed_hypothesis <= borrowed_premise:
    # check if the estimate of 'borrowed_hypothesis' contradicts the amount borrowed in the premise
    label = "contradiction"
else:
    # if the hypothesis value and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
