rd_top_premise = 15
rd_top_hypothesis = 65
class_size_premise = 182
class_size_hypothesis = 182

# the hypothesis talks about Veena's rank in a class, referenced also in the premise
if rd_top_hypothesis <= rd_top_premise:
    # check if the hypothesis value contradicts the estimate of more than 'rd_top_premise'
    label = "contradiction"
elif class_size_hypothesis!= class_size_premise:
    # check if the class size in the hypothesis contradicts the class size reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for Veena's rank
    # any rank greater than 'rd_top_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
