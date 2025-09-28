from vllm import LLM, SamplingParams

# GPU에서 모델 불러오기
llm = LLM(model="gpt2")

# 샘플 프롬프트 정의
prompt = "Hello, my name is"

# 샘플링 파라미터
params = SamplingParams(max_tokens=50)

# 모델 실행
output = llm.generate(prompt, params)

