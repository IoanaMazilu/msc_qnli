saving_decrease_premise = 80
saving_decrease_hypothesis = 30

# the hypothesis talks about the decrease in saving amount, which is also mentioned in the premise
if saving_decrease_hypothesis >= saving_decrease_premise:
    # check if the hypothesis value contradicts the estimate of less than'saving_decrease_premise'
    label = "contradiction"
elif saving_decrease_hypothesis < saving_decrease_premise:
    # if the hypothesis value is less than the premise value, it does not contradict the premise
    # but it cannot be explicitly entailed from the premise either
    label = "neutral"

print(label)
