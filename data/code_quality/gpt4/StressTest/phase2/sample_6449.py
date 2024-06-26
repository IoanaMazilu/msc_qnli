john_years_premise = 5
john_years_hypothesis = 7

# the hypothesis talks about the years when John will be twice as old as Frank, also referenced in the premise
# since the years are different, it is impossible for both the premise and the hypothesis to be true
# thus, this is a contradiction
if john_years_premise != john_years_hypothesis:
    label = "contradiction"
else:
    label = "neutral"

print(label)
