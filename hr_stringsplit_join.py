"""
    # 100daysCodingChallenge - Day 3
    Level: Easy

    Just split the string with spaces and then join them with dashes
"""

def split_and_join(line):
    line = line.split(" ")
    a = "-".join(line)

    return a

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
