# 意图识别
#encoding=utf-8
from torch.xpu import device
from transformers import AutoModelForCausalLM, AutoTokenizer
import json
from tqdm import tqdm

device = "cuda" # the device to load the model onto


# 修改模型路径
model_name = '/Users/coderpwh/quickstart/large_language-model_train_20250519_negm/model/'
print(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained(model_name)

count = 0
ecount = 0


# 修改训练数据路径
test_data = json.load(open('/Users/coderpwh/python/workspace/pythonProject/testdata.json'))
system_prompt = '你是一个意图识别专家，可以根据用户的问题识别出意图，并返回对应的函数调用和参数。'

for i in tqdm(test_data[:]):
    prompt = '<|im_start|>system\n' + system_prompt + '<|im_end|>\n<|im_start|>user\n' + i['instruction'] + '<|im_end|>\n<|im_start|>assistant\n'
    gold = i['output']
    gold = gold.split(';')[0] if ';' in gold else gold

    model_inputs = tokenizer([prompt], return_tensors="pt").to(device)
    generated_ids = model.generate(
        model_inputs.input_ids,
        max_new_tokens=64,
        pad_token_id=tokenizer.eos_token_id,
        eos_token_id=tokenizer.eos_token_id,
        do_sample=False
    )
    generated_ids = [
        output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
    ]
    pred = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
    if gold.split('(')[0] == pred.split('(')[0]:
        count += 1
        gold_list = set(gold.strip()[:-1].split('(')[1].split(','))
        pred_list = set(pred.strip()[:-1].split('(')[1].split(','))
        if gold_list == pred_list:
            ecount += 1
    else:
        pass

print("意图识别准确率：", count/len(test_data))
print("参数识别准确率：", ecount/len(test_data))
