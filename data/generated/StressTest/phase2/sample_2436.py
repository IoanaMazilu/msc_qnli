# Premise: In an exam, Amar scored 64 percent, Bhavan scored 36 percent and Chetan 44 percent.
# Hypothesis: In an exam, Amar scored more than 54 percent, Bhavan scored 36 percent and Chetan 44 percent.
# Golden Label: entailment

amar_score_premise = 64
amar_score_hypothesis = 54
bhavan_score_premise = 36
bhavan_score_hypothesis = 36
chetan_score_premise = 44
chetan_score_hypothesis = 44

# the hypothesis talks about the exam scores of Amar, Bhavan and Chetan mentioned in the premise
if amar_score_hypothesis > amar_score_premise:
    # check if the hypothesis value contradicts the value of 'amar_score_premise'
    label = "contradiction"
elif bhavan_score_hypothesis != bhavan_score_premise:
    # check if the value of 'bhavan_score_hypothesis' contradicts the value of 'bhavan_score_premise'
    label = "contradiction"
elif chetan_score_hypothesis != chetan_score_premise:
    # check if the value of 'chetan_score_hypothesis' contradicts the value of 'chetan_score_premise'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

