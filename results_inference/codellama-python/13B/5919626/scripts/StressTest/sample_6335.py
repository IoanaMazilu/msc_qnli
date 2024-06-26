man_dollars_premise = 1000
man_dollars_hypothesis = 1000

# the hypothesis talks about the number of dollars the man has
# the premise gives the exact number of dollars the man has
if man_dollars_premise!= man_dollars_hypothesis:
    # check if the hypothesis value contradicts the exact number of dollars the man has
    label = "contradiction"
else:
    # the premise gives the exact number of dollars the man has
    # the hypothesis talks about the same exact number of dollars the man has
    label = "entailment"

print(label)
