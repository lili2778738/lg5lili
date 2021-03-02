import yaml


def data():
    with open("member.yaml", 'rb') as f:
        datas = yaml.safe_load(f)
        return datas
if __name__ == '__main__':
    a=data()
