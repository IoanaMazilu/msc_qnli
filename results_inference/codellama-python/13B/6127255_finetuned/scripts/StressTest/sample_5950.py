#T_premise = 20
#T_hypothesis = 20
#K_premise = (T_premise / (2/9)) + 32
#K_hypothesis = (T_hypothesis / (5/9)) + 32

# the hypothesis talks about the same situation as the premise, but with a different formula
# we need to check if the calculated value of K from the hypothesis contradicts the calculated value from the premise
if K_premise!= K_hypothesis:
    label = "contradiction"
else:
    label = "neutral"

print(label)
#