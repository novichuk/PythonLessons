def read_file(path) -> str:
    # path = '../requirements.txt'
    requirements_file = open(path, 'r')
    requirements = requirements_file.read()
    requirements_file.close()
    return requirements
