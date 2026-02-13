import ollama


# https://ollama.com/aryanvala/hushiyar-lite
class Response_Ollama:

    def buildingPrompt(studentData, priorityData):
        with open('prompt.txt', 'r') as file:
            content = file.read()

        # format the priorityData dictionary
        # puts priorities on different lines and numbers them from 1 to 4
        priorityStr = "\n".join([f"{rank + 1}. {habit}" for rank, habit in sorted(priorityData.items())])

        # put into the first dictionary to make it easier to put into the file
        studentData["Priorities"] = priorityStr
        # put data into file (you now have your full prompt)
        prompt = content.format(**studentData)
        return prompt

    def modelResponse(prompt):
        # ollama code right here to get response from specific model
        response = ollama.chat(
            model="aryanvala/hushiyar-lite",
            messages=[{"role": "user", "content": prompt}]
        )

        # return response to display to user later
        return response["message"]["content"]
