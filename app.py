import transformers
from transformers import DistilBertTokenizer
from transformers import TFDistilBertForSequenceClassification
from transformers import TextClassificationPipeline

import tensorflow as tf
import pandas as pd
import json
import gc

from sklearn.model_selection import train_test_split
save_directory = "saved_models"
tokenizer_fine_tuned = DistilBertTokenizer.from_pretrained(save_directory)

model_fine_tuned = TFDistilBertForSequenceClassification.from_pretrained(save_directory)
test_text="virgin blue shares plummet 20% shares in australian budget airline virgin blue plunged 20% after it warned of a steep fall in full year profits.  virgin blue said profits after tax for the year to march would be between 10% to 15% lower than the previous year.  sluggish demand reported previously for november and now december 2004 continues   said virgin blue chief executive brett godfrey. virgin blue  which is 25% owned by richard branson  has been struggling to fend off pressure from rival jetstar. it cut its full year passenger number forecast by  approximately 2.5% . virgin blue reported a 22% fall in first quarter profits in august 2004 due to tough competition. in november  first half profits were down due to slack demand and rising fuel costs. virgin blue was launched four years ago and now has roughly one third of australia s domestic airline market. but the national carrier  qantas  has fought back with its own budget airline  jetstar  which took to the skies in may 2004. sydney-listed virgin blue s shares recovered slightly to close 12% down on wednesday. shares in its major shareholder  patrick corporation - which owns 46% of virgin blue - had dropped 31% by the close."
predict_input = tokenizer_fine_tuned.encode(
    test_text,
    truncation = True,
    padding = True,
    return_tensors = 'tf'
)

output = model_fine_tuned(predict_input)[0]

prediction_value = tf.argmax(output, axis = 1).numpy()[0]

print(prediction_value)