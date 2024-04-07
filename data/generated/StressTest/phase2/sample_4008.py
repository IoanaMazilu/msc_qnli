# Premise: Lindy runs at a constant speed of 10 feet per second from Christina to Jack, back to Christina, back to Jack, and so forth.
# Hypothesis: Lindy runs at a constant speed of less than 50 feet per second from Christina to Jack, back to Christina, back to Jack, and so forth.
# Golden Label: entailment

lindy_speed_premise = 10
lindy_speed_hypothesis = 50

# the hypothesis talks about the speed at which Lindy runs, referenced also in the premise
if lindy_speed_premise >= lindy_speed_hypothesis:
    # check if the constant speed of Lindy in the premise contradicts the estimate of less than 'lindy_speed_hypothesis'
    label = "contradiction"
else:
    # if the speed value in the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)

