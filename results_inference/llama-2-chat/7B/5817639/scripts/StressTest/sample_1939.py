lawn_rake_premise = 60
lawn_rake_hypothesis = 30

# the hypothesis talks about the time it takes to rake a lawn, which is also referred to in the premise
if lawn_rake_hypothesis <= lawn_rake_premise:
    # check if the hypothesis value contradicts the estimate of less than 'lawn_rake_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the time it takes to rake a lawn, and the hypothesis value is consistent with that estimate
    label = "entailment"

print(label)
