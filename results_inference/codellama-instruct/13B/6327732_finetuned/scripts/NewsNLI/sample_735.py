# define variables for the numerical entities in the premise and hypothesis
premise_ten_cate_position = "assistant manager"
hypothesis_ten_cate_position = "assistant coach"

# check if the position in the hypothesis contradicts the position in the premise
if hypothesis_ten_cate_position!= premise_ten_cate_position:
    label = "contradiction"
else:
    label = "neutral"

print(label)
