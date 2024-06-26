efficiency_premise = 55
efficiency_hypothesis = 25

# the hypothesis talks about the efficiency of Tanya compared to Sakshi, referenced also in the premise
if efficiency_hypothesis > efficiency_premise:
    # check if the efficiency in the hypothesis contradicts the premise where Tanya is less than 'efficiency_premise' % more efficient than Sakshi
    label = "contradiction"
elif efficiency_hypothesis < efficiency_premise:
    # check if the efficiency in the hypothesis is less than the 'efficiency_premise' %, which would entail the premise
    label = "entailment"
else:
    # if the efficiency is exactly 'efficiency_premise' %, it cannot be less than 'efficiency_premise' %, so it is neutral
    label = "neutral"

print(label)
