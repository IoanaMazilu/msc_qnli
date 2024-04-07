# Premise: Jasmine has a toaster with two slots that toasts one side of each piece of bread at a time, and it takes one minute to do so. If she wants to make 3 pieces of toast, what is the least amount of time she needs to toast them on both sides?
# Hypothesis: Jasmine has a toaster with two slots that toasts one side of each piece of bread at a time, and it takes one minute to do so. If she wants to make less than 8 pieces of toast, what is the least amount of time she needs to toast them on both sides?
# Golden Label: entailment

toast_premise = 3
toast_hypothesis = 8

# the hypothesis talks about the number of toast pieces, referenced also in the premise
if toast_hypothesis < toast_premise:
    # check if the hypothesis value contradicts the number of toast pieces in the premise
    label = "contradiction"
elif toast_hypothesis == toast_premise:
    # check if the hypothesis value can be fully entailed from the premise
    label = "entailment"
else:
    # the premise gives only a specific number of toast pieces
    # any number of toast pieces less than 'toast_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

