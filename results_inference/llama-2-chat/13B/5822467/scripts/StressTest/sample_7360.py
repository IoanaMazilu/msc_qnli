boys_age14_premise = 20
boys_age14_hypothesis = 80
boys_age15_premise = 70
boys_age15_hypothesis = 70
boys_age13_premise = 50
boys_age13_hypothesis = 50
boys_age12_premise = 60

# check if the hypothesis values and estimates do not contradict the premise ones
if boys_age14_hypothesis <= boys_age14_premise and \
   boys_age15_hypothesis == boys_age15_premise and \
   boys_age13_hypothesis == boys_age13_premise and \
   boys_age12_hypothesis == boys_age12_premise:
    # all values and estimates are consistent, so we can infer entailment
    label = "entailment"
elif boys_age14_hypothesis > boys_age14_premise or \
     boys_age15_hypothesis > boys_age15_premise or \
     boys_age13_hypothesis > boys_age13_premise or \
     boys_age12_hypothesis > boys_age12_premise:
    # at least one aspect in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, but we cannot explicitly entail the hypothesis from the premise
    # then the relation is neutral
    label = "neutral"

print(label)
