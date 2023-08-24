# send contents to makersuite api for improvement, better data for chat

import pprint
import google.generativeai as palm

# -----------------------------------------------------------------------------
out_file = "improve.txt" # file where improved text is written to
user_api_key = "#####" # enter your makersuite key in cmd line
exec(open('configurator.py').read()) # cmd overwrite
# -----------------------------------------------------------------------------

palm.configure(api_key=user_api_key)

#get text bison
models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name

def improve():
  prompt = """
  You are an expert at solving word problems.
  
  Solve the following problem:
  
  I have three houses, each with three cats.
  each cat owns 4 mittens, and a hat. Each mitten was
  knit from 7m of yarn, each hat from 4m.
  How much yarn was needed to make all the items?
  
  Think about it step by step, and show your work.
  """

  completion = palm.generate_text(
      model=model,
      prompt=prompt,
      temperature=0,
      # The maximum length of the response
      max_output_tokens=800,
  )
  
  print(completion.result)
