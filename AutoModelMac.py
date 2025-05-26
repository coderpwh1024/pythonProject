# encoding=utf-8
from transformers import AutoModelForCausalLM, AutoTokenizer
import json
from tqdm import tqdm
import torch  # 添加torch引用

# 配置Apple Silicon GPU支持
device = "mps" if torch.backends.mps.is_available() else "cpu"
print(f"Using device: {device}")

# 修改模型路径
model_name = '/Users/coderpwh/quickstart/large_language-model_train_20250519_negm/model/'
print("Loading model: {model_name}")

# 使用更节省内存的方式加载模型
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16,  # 使用半精度减少内存占用
    device_map="auto",
    low_cpu_mem_usage=True  # 优化内存使用
).to(device)

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
    print("pred:",pred)
    print("gold:",gold)
    print("结果1:", gold.split('(')[0])
    print("结果2:", pred.split('(')[0])
    if gold.split('(')[0] == pred.split('(')[0]:
        count += 1
        gold_list = set(gold.strip()[:-1].split('(')[1].split(','))
        pred_list = set(pred.strip()[:-1].split('(')[1].split(','))
        if gold_list == pred_list:
            ecount += 1
    else:
        pass

print("ecount:",ecount)
print("count:",count)
print("意图识别准确率：", count/len(test_data))
print("参数识别准确率：", ecount/len(test_data))