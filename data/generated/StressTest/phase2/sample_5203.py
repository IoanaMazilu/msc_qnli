# Premise: If Dana gives her parents less than 6% of that amount back each month, how much will she still owe her parents after four years of college?
# Hypothesis: If Dana gives her parents 2% of that amount back each month, how much will she still owe her parents after four years of college?
# Golden Label: neutral

percentage_premise = 6
percentage_hypothesis = 2

# the hypothesis talks about the percentage of the amount Dana gives back to her parents each month, referenced also in the premise
if percentage_hypothesis >= percentage_premise:
    # check if the hypothesis value contradicts the estimate of less than 'percentage_premise'
    label = "contradiction"
else:
    # the premise gives an upper limit for the percentage of amount Dana gives back
    # any percentage less than 'percentage_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

