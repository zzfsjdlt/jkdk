import argparse


parser = argparse.ArgumentParser(description='Process some strings.')
parser.add_argument('-c', '--credit', required=True, help='学号')
parser.add_argument('-p', '--password', required=True, help='密码')

credit = parser.parse_args()
print(credit.credit)
print(credit.password)
