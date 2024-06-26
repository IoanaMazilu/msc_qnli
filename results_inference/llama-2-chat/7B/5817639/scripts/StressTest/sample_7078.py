page_count_premise = 56
page_count_hypothesis = 66

# the hypothesis talks about the number of pages in a history paper, referenced also in the premise
if page_count_hypothesis <= page_count_premise:
    # check if the hypothesis value contradicts the estimate of more than 'page_count_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of pages
    # any number of pages greater than 'page_count_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
