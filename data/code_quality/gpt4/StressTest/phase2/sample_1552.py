join_month_premise = 5
join_month_hypothesis = 2

# the hypothesis talks about the time when Jose joined him, referenced also in the premise
if join_month_hypothesis > join_month_premise:
    # check if the hypothesis value contradicts the premise of less than 'join_month_premise'
    label = "contradiction"
elif join_month_hypothesis <= join_month_premise:
    # the premise gives only an estimate for the joining time
    # any time less than 'join_month_premise' is consistent with the premise and can be entailed
    label = "entailment"

print(label)
