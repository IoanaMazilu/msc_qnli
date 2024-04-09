cats_premise = 17.0
cats_given_premise = 14.0
cats_hypothesis = 5.0

# the hypothesis refers to the number of cats, which are also mentioned in the premise
# compute the difference between the number of cats in the premise and the number of cats in the hypothesis
diff = cats_premise - cats_hypothesis

if diff > 0:
    # if the number of cats in the hypothesis is less than the number of cats in the premise, we can infer entailment
    label = "entailment"
elif diff == 0:
    # if the number of cats in the hypothesis is equal to the number of cats in the premise, we can infer neutrality
    label = "neutral"
else:
    # if the number of cats in the hypothesis is greater than the number of cats in the premise, we can infer contradiction
    label = "contradiction"

print(label)
