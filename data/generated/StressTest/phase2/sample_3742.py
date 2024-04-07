# Premise: Caleb spends $70.50 on less than 60 hamburgers for the marching band.
# Hypothesis: Caleb spends $70.50 on 50 hamburgers for the marching band.
# Golden Label: neutral

spend_premise = 70.50
hamburgers_premise = 60
spend_hypothesis = 70.50
hamburgers_hypothesis = 50

# the hypothesis talks about the amount of money spent and number of hamburgers, which are also mentioned in the premise
if hamburgers_hypothesis >= hamburgers_premise:
    # check if the number of hamburgers in the hypothesis contradicts the estimate of less than 'hamburgers_premise'
    label = "contradiction"
elif spend_hypothesis != spend_premise:
    # check if the amount of money spent in the hypothesis contradicts the amount of money spent reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

