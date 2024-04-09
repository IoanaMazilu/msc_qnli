john_age_premise = 5
john_age_hypothesis = 8
frank_age_premise = 0

# the hypothesis talks about John's age in relation to Frank's age, referenced also in the premise
if john_age_hypothesis <= (2 * john_age_premise):
    # check if the hypothesis value contradicts the estimate of John's age in the premise
    label = "contradiction"
elif frank_age_premise!= 0:
    # check if the premise value of Frank's age contradicts the hypothesis value
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
