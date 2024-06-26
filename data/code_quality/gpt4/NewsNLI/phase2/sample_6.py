capsized_times_premise = 2
capsized_times_hypothesis = 3

# the hypothesis mentions the number of times the boat capsized, which is also referenced in the premise
# however, the hypothesis refers to total number of capsizes while the premise refers to additional capsizes
if capsized_times_hypothesis <= capsized_times_premise:
    # check if the number of times the boat capsized in the hypothesis is less than or equal to the number of additional capsizes in the premise
    label = "contradiction"
else:
    # if the number of times the boat capsized in the hypothesis exceeds the number of additional capsizes in the premise, we cannot infer entailment or contradiction
    label = "neutral"

print(label)
