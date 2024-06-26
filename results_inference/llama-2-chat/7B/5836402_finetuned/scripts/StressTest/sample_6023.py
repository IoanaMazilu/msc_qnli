borrowed_pounds_premise = 5000
borrowed_pounds_hypothesis = 3000

# the hypothesis talks about the amount Dana borrows annually for her college education, which is also mentioned in the premise
if borrowed_pounds_hypothesis!= borrowed_pounds_premise:
    # check if the amount borrowed in the hypothesis contradicts the amount borrowed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
