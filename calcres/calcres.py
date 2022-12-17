from settings import ROOT, CONF_PATH
from src.flow import configure_app, calculate
from src.flow.output import print_sum, print_content


def main():
    data = configure_app(ROOT, CONF_PATH)

    c1 = calculate(name='арматура', quantity=1, data=data)
    c2 = calculate(name='синий экстракт', quantity=1, data=data)

    print_content(c1)
    print_content(c2)
    print_sum(c1, c2)


if __name__ == '__main__':
    main()
