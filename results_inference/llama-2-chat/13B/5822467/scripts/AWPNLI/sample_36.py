hamburgers_premise = 9.0
served_hamburgers_premise = 3.0
left_over_hamburgers_hypothesis = 6.0

# the hypothesis talks about the number of left over hamburgers, which is also referenced in the premise
# compute the difference between the number of hamburgers served and the number of hamburgers left over
diff = served_hamburgers_premise - left_over_hamburgers_hypothesis

if diff > 0:
    # if the number of hamburgers served is greater than the number of hamburgers left over, we can infer entailment
    label = "entailment"
elif diff == 0:
    # if the number of hamburgers served is equal to the number of hamburgers left over, we can infer neutrality
    label = "neutral"
else:
    # if the number of hamburgers served is less than the number of hamburgers left over, we can infer contradiction
    label = "contradiction"

print(label)
