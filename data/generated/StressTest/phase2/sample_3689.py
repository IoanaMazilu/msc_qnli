# Premise: Jasmine has a toaster with two slots that toasts one side of each piece of bread at a time, and it takes one minute to do so. If she wants to make 3 pieces of toast, what is the least amount of time she needs to toast them on both sides?
# Hypothesis: Jasmine has a toaster with two slots that toasts one side of each piece of bread at a time, and it takes one minute to do so. If she wants to make more than 3 pieces of toast, what is the least amount of time she needs to toast them on both sides?
# Golden Label: contradiction

toast_premise = 3
toast_hypothesis = 3

# the hypothesis talks about the number of toasts Jasmine wants to make, referenced also in the premise
if toast_hypothesis > toast_premise:
    # check if the hypothesis value contradicts the exact number of 'toast_premise'
    label = "contradiction"
else:
    # the premise gives an exact number of toasts
    # the hypothesis does not contradict the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

