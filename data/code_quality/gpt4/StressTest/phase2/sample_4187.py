baseball_fans_premise = 352
baseball_fans_hypothesis = 352

# the hypothesis talks about the number of baseball fans in a town, referenced also in the premise
if baseball_fans_hypothesis > baseball_fans_premise:
    # check if the hypothesis value contradicts with the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
