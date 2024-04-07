# Premise: Ram and Shyam can do together a piece of work in 20 days.
# Hypothesis: Ram and Shyam can do together a piece of work in 30 days.
# Golden Label: contradiction

work_days_premise = 20
work_days_hypothesis = 30

# the hypothesis talks about the number of days Ram and Shyam can do a piece of work, referenced also in the premise
if work_days_hypothesis == work_days_premise:
    # check if the number of days in the hypothesis is the same as in the premise
    label = "entailment"
else:
    # the number of days Ram and Shyam can do a piece of work is not the same in the hypothesis and the premise
    label = "contradiction"

print(label)

