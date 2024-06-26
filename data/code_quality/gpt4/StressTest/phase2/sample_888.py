saving_decrease_percentage_premise = 40
saving_decrease_percentage_hypothesis = 70

# the hypothesis is about the decrease in savings amount, also mentioned in the premise
if saving_decrease_percentage_hypothesis < saving_decrease_percentage_premise:
    # check if the hypothesis value contradicts the reported 'saving_decrease_percentage_premise'
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, but does not fully entail it, the relation is neutral
    label = "neutral"

print(label)
