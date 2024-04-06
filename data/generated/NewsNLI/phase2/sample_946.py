# Premise: Portuguese league leaders FC Porto secured a 1-0 victory at Russian club CSKA Moscow in their round of 16 clash, thanks to a 70th-minute strike from Colombian striker Freddy Guarin.
# Hypothesis: Porto beat CSKA Moscow 1-0, while Rangers draw 0-0 at PSV Eindhoven.
# Golden Label: neutral

porto_score_premise = 1
porto_score_hypothesis = 1
cska_score_premise = 0
cska_score_hypothesis = 0

# the hypothesis mentions the score between Porto and CSKA Moscow, which is also mentioned in the premise
if porto_score_hypothesis != porto_score_premise:
    # check if the score of Porto in the hypothesis contradicts the score reported in the premise
    label = "contradiction"
elif cska_score_hypothesis != cska_score_premise:
    # check if the score of CSKA Moscow from the hypothesis contradicts the score in the premise
    label = "contradiction"
else:
    # if the hypothesis scores do not contradict the premise scores, we can infer entailment
    label = "entailment"

print(label)

