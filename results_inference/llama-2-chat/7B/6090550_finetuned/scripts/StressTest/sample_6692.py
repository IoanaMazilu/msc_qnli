y_premise = 1800
y_hypothesis = 7800

# the hypothesis talks about the distance travelled by air, which is also mentioned in the premise
if y_hypothesis!= y_premise:
    # check if the distance travelled by air in the hypothesis contradicts the distance travelled by air in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
