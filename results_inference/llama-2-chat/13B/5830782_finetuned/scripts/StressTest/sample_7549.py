saving_decrease_premise = 80
saving_decrease_hypothesis = 30

# the hypothesis refers to the decrease in savings mentioned in the premise
if saving_decrease_hypothesis >= saving_decrease_premise:
    # check if the decrease percentage in the hypothesis contradicts the decrease percentage in the premise
    label = "contradiction"
elif saving_decrease_hypothesis < saving_decrease_premise:
    # check if the decrease percentage in the hypothesis is less than the decrease percentage in the premise
    # any decrease percentage less than'saving_decrease_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
