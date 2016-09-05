import yaml


def read_yaml(file_name):
    try:
        with open(file_name, 'r') as f:
            doc = yaml.load(f)
        return {key: value for key, value in doc.items() if value is not None}
    except IOError as e:
        print 'File: %s does not exist' % file_name
