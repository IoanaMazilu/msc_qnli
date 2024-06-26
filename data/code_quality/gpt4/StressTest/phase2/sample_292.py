committees_premise = 4
committees_hypothesis = 3

# the hypothesis talks about the number of people in a committee, also referenced in the premise
if committees_hypothesis >= committees_premise:
    # check if the hypothesis value contradicts the estimate of less than 'committees_premise'
    label = "contradiction"
elif committees_hypothesis < committees_premise:
    # if the number of people in a committee in the hypothesis is less than 'committees_premise', it's entailed from the premise
    label = "entailment"

print(label)
