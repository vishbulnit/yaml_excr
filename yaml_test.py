import yaml

print("This is to test yaml script.")

with open('yaml_script2.yaml', 'r') as file:
    try:
        print(yaml.safe_load(file))
    except yaml.YAMLError as exc:
        print(exc)
    
