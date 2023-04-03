import json
from awslambda import *

def load_sample_event_from_file( test_event_file_name: str) -> dict:
    """
        Loads and validate test events from the file system
        """
    event_file_name = f"aws/test events/{test_event_file_name}.json"
    with open(event_file_name, "r", encoding='UTF-8') as file_handle:
        event = json.load(file_handle)
        #validate(event=event, schema=INPUT_SCHEMA)
        return event

test_event = load_sample_event_from_file("sample")

for kvp in test_event:
    print(kvp)
    print(test_event[kvp])

test_return_value = lambda_handler(event=test_event, context=None)