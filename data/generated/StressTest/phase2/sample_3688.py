# Premise: Jasmine has a toaster with two slots that toasts one side of each piece of bread at a time, and it takes one minute to do so. If she wants to make less than 8 pieces of toast, what is the least amount of time she needs to toast them on both sides?
# Hypothesis: Jasmine has a toaster with two slots that toasts one side of each piece of bread at a time, and it takes one minute to do so. If she wants to make 3 pieces of toast, what is the least amount of time she needs to toast them on both sides?
# Golden Label: neutral

toast_pieces_premise = 8
toast_pieces_hypothesis = 3

# the hypothesis refers to the number of toast pieces mentioned in the premise
if toast_pieces_hypothesis >= toast_pieces_premise:
    # check if the number of toast pieces in the hypothesis contradicts the estimate of less than 'toast_pieces_premise'
    label = "contradiction"
elif toast_pieces_hypothesis < toast_pieces_premise:
    # the premise gives an estimate for the number of toast pieces
    # any number of toast pieces less than 'toast_pieces_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

