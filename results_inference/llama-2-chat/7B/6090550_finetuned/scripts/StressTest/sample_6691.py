y_premise = 8800
y_hypothesis = 1800

# the hypothesis talks about the distance travelled by air, which is also mentioned in the premise
if y_hypothesis >= y_premise:
    # check if the distance travelled by air in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the distance travelled by air in the hypothesis is less than the distance travelled by air in the premise, we can infer entailment
    label = "entailment"

print(label)
