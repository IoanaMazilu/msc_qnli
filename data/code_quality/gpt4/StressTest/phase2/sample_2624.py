baseball_fans_premise = 390
baseball_fans_hypothesis = 390

# The hypothesis refers to the number of baseball fans in the town mentioned in the premise
if baseball_fans_hypothesis >= baseball_fans_premise:
    # Check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)