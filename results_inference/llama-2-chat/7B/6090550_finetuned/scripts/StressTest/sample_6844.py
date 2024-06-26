y_sacha_premise = 4
y_sacha_hypothesis = 7
y_bruno_premise = 5
y_bruno_hypothesis = 5

# the hypothesis talks about the running speed of Sacha and Bruno, which is also mentioned in the premise
if y_sacha_hypothesis <= y_sacha_premise:
    # check if the hypothesis value for Sacha's running speed contradicts the premise
    label = "contradiction"
elif y_bruno_hypothesis!= y_bruno_premise:
    # check if the hypothesis value for Bruno's running speed contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

