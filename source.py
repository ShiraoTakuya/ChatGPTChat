import datetime
import pickle
import openai

openai.api_key = open(open("SET.INI").read()).read()

class ChatGPT:
	def __init__(self, gpt_ver, role):
		self.gpt_ver = gpt_ver
		self.role = role
		self.history = [{"role":"system","content":"You are a "+role}]

	def generate_text(self, prompt):
		self.history.append({"role":"user","content":prompt})
		completion = openai.ChatCompletion.create(
			model=self.gpt_ver,
			max_tokens=1000,
			messages=self.history
		)
		message = completion.choices[0].message.content
		self.history.append({"role":"assistant","content":message})

		return completion.choices[0].message.content

if __name__ == "__main__":
	input_prompt = input("new？(y/n):")
	if input_prompt.lower() == 'y':
		role = input("role?:")
		gpt_ver = input("ver?(gpt-3.5-turbo/gpt-4):")
		gpt_a = ChatGPT(gpt_ver, role)
		now = datetime.datetime.now()
		str_datetime = now.strftime("%Y%m%d%H%M%S")
		file_name = str_datetime+".pkl"
	else:
		file_name = input("pickle name?:")
		with open(file_name, "rb") as file:
			gpt_a = pickle.load(file)

	while True:
		input_prompt = input("question？:")
		if input_prompt.lower() == 'q':
			break
		print(gpt_a.generate_text(input_prompt))
		with open(file_name, "wb") as file:
			pickle.dump(gpt_a, file)
