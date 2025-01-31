import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data("animals_data.json")

def get_animal_name():
    for i in animals_data:
        skip_type = i.get("characteristics", {}).get("type", "Unknown")
        if skip_type == "Unknown":
            print(f"Name: {i["name"]}\n"
                  f"Diet: {i["characteristics"]["diet"]}\n"
                  f"Location: {i["locations"][0]}")
        else:
            print(f"Name: {i["name"]}\n"
                  f"Diet: {i["characteristics"]["diet"]}\n"
                  f"Location: {i["locations"][0]}\n"
                  f"Type: {i["characteristics"]["type"]}")






get_animal_name()