
import os

from groq import Groq

import json
def sorter(input_folder_path, user_prompt):
  # lists the files of a specified folder as a string
  def list(folder):
      # lists the file as a "LIST"
      f = os.listdir(folder)
      # converts the list into a string with each file name on a new linie for a cleaner prompt
      files = "\n".join(f)
      return files
  #uses a local variable to store the files as a string of the desired folder
  file_list_string = list(input_folder_path)

  #API stuff
  client = Groq(api_key="your_api_key")
  final_prompt = f"""
  You are a file organization assistant.

  User request:
  {user_prompt}

  Files:
  {file_list_string}

  Return a JSON object where keys are category names and values are lists of filenames.

  Place each file in the correct category.
  Return ONLY valid JSON.
  Do not include explanations or text.
  Do not include markdown.
  You must use the exact filenames from the list below.
  Do not modify the filenames.
  Do not create new filenames.
  Every file must appear in exactly one category.
  Do not omit any files.
  Use the filenames exactly as provided.  
  """
  response = client.chat.completions.create(
      model="llama-3.1-8b-instant",
      messages=[
          {
              "role": "user",
              "content": final_prompt
          }
      ],
      max_tokens=2000,
      response_format={"type": "json_object"}
  )


  '''
  result is a object out of which the response is to be extracted
  the format of the result looks something like this - 
    {
    "id": "chatcmpl-abc123",
    "object": "chat.completion",
    "created": 1710000000,
    "model": "llama-3-70b",
    "choices": [
        {
        "index": 0,
        "message": {
            "role": "assistant",
            "content": "{\"finance\": [\"revenue\", \"profit\"], \"hr\": [\"employee\", \"salary\"]}"
        },
        "finish_reason": "stop"
        }
    ],
    "usage": {
        "prompt_tokens": 120,
        "completion_tokens": 45,
        "total_tokens": 165
    }
    }
  '''
  result = response.choices[0].message.content
  categories = json.loads(result)
  return(categories)  