import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data("animals_data.json")

def get_animal_name():
    output = []
    for i in animals_data:
        skip_type = i.get("characteristics", {}).get("type", "Unknown")
        if skip_type == "Unknown":
            output.append(f"Name: {i["name"]}\n"
                          f"Diet: {i["characteristics"]["diet"]}\n"
                          f"Location: {i["locations"][0]}")

        else:
            output.append(f"Name: {i["name"]}\n"
                          f"Diet: {i["characteristics"]["diet"]}\n"
                          f"Location: {i["locations"][0]}\n"
                          f"Type: {i["characteristics"]["type"]}")

    result = "\n\n".join(output)
    return result


def read_html(file_path):
    with open(file_path, "r") as f:
        file_str = f.read()
        return file_str


html_file = str(read_html("animals_template.html"))
animals_str = str(get_animal_name())

new_html = html_file.replace("__REPLACE_ANIMALS_INFO__", animals_str)

with open("animals.html", "w") as f:
    f.write(new_html)