# Premise: For how many days did the trial last, if each patient received a total amount of less than 545 milligrams of Dosaxin during the whole trial?
# Hypothesis: For how many days did the trial last, if each patient received a total amount of 145 milligrams of Dosaxin during the whole trial?
# Golden Label: neutral

dosaxin_premise = 545
dosaxin_hypothesis = 145

# the hypothesis talks about the amount of Dosaxin given to each patient, referenced also in the premise
if dosaxin_hypothesis >= dosaxin_premise:
    # check if the hypothesis value contradicts the estimate of less than 'dosaxin_premise'
    label = "contradiction"
elif dosaxin_hypothesis < dosaxin_premise:
    # the premise gives only an estimate for the amount of Dosaxin
    # any amount of Dosaxin less than 'dosaxin_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "entailment"
else:
    label = "neutral"

print(label)

