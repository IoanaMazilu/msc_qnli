baseball_fans_premise = 390
baseball_fans_hypothesis = 490

# the hypothesis talks about the number of baseball fans in a town, which is also referenced in the premise
if baseball_fans_hypothesis < baseball_fans_premise:
    # check if the hypothesis value contradicts the exact number of 'baseball_fans_premise'
    label = "contradiction"
elif baseball_fans_hypothesis > baseball_fans_premise:
    # check if the number of baseball fans in the hypothesis contradicts the exact number of baseball fans reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
