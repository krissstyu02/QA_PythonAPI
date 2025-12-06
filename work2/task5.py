import json

string_as_json_format = '{"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}'
obj = json.loads(string_as_json_format)


messages_list = obj["messages"]


second_message_text = messages_list[1]["message"]
print(second_message_text)
