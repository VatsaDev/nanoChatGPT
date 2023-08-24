# send contents to makersuite api for improvement, better data for chat

import pprint
import google.generativeai as palm

out_file = "improve.txt" # file where improved text is written to

def improve(text_improve, user_api_key):
  palm.configure(api_key=user_api_key)
  
  #get text bison
  models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
  model = models[0].name

  prompt = "Return Chat conversation improved ```"+text_improve+"```"

  completion = palm.generate_text(
      model=model,
      prompt=prompt,
      temperature=0.1,
      # The maximum length of the response
      max_output_tokens=800,
  )

  with open("improve.txt", "w") as f:
    f.write(completion.result) # sent to improve.txt
  
  return completion.result
