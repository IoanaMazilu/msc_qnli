y_premise = 38
y_hypothesis = 28

# the hypothesis talks about the time Dawson took to run the first leg of the course, referenced also in the premise
if y_hypothesis >= y_premise:
    # check if the hypothesis value contradicts the time stated in the premise
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise value, we can infer entailment
    label = "entailment"

print(label)
