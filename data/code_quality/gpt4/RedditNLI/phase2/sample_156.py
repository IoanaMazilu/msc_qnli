boost_premise = 720
stimulus_hypothesis = 720

# the hypothesis and premise mention a monetary gain from falling gas prices
if boost_premise != stimulus_hypothesis:
    # check if the gain in the hypothesis contradicts the gain in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
