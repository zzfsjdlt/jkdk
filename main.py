from jkdk import Jkdk
import os
# import argparse

# parser = argparse.ArgumentParser(description='填入学号和密码')
# parser.add_argument('-c', '--credit', required=True, help='学号')
# parser.add_argument('-p', '--password', required=True, help='密码')

# outputs = parser.parse_args()
# print(f'credit={outputs.credit}, password={outputs.password}')

username = os.environ.get('username')
password = os.environ.get('password')

m = Jkdk(username, password)
m.jkdk()
