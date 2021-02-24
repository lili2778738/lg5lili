import yaml


def yada():
    with open("../src/main_page_data.yml", "rb") as f:
        datas = yaml.safe_load(f)
        data = datas['handle']
        print(data)
        for everydata in data:
            action = everydata['lactor']
            print(action)

if __name__ == '__main__':
    a=yada()