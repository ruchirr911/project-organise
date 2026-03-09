
import os

from groq import Groq

import json
def sorter(input_folder_path, user_prompt):
  # lists the files of a specified folder
  def list(folder):
      f = os.listdir(folder)
      files = "\n".join(f)
      return files
  
  file_list_string = list(input_folder_path)

  client = Groq(api_key="your_api_key_here")
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

  result = response.choices[0].message.content
  categories = json.loads(result)
  return(categories)  