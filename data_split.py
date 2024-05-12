import os
import numpy
import json
import os.path as osp
import time


def read_json(fpath):
    """Read json file from a path."""
    with open(fpath, 'r') as f:
        obj = json.load(f)
    return obj

def write_json(obj, fpath):
    """Writes to a json file."""
    # if not osp.exists(osp.dirname(fpath)):
    #     os.makedirs(osp.dirname(fpath))
    with open(fpath, 'w') as f:
        json.dump(obj, f, indent=4, separators=(',', ': '))

def main():
    start_time = time.time()  # 记录开始时间
    json_path = r'Headline\test.json'
    obj = read_json(json_path)
    cnt = 0

    # dict1 = {}
    list1 = []
    for item in obj:

        sections = item['input'].split('\n\n')

        # print(sections)
        for i, section in enumerate(sections):
            # Answer is "No"
            if section[-2] == "N" and section[-1] == "o":
                cnt += 1
                answer = "No"
                question = section[:-2]
                # print(section)
            # Answer is "Yes"
            elif section[-3] == "Y" and section[-2] == "e" and section[-1] == "s":
                cnt += 1
                answer = "Yes"
                question = section[:-3]
                # print(section)
            # No response
            else: continue

            dict1 = {
                "id": item['id'],
                "Question": question,
                "Answer": answer
            }
            list1.append(dict1)
        # break
    write_json(list1, 'a.json')
    # print(obj[0])
    end_time = time.time()  # 记录结束时间
    execution_time = end_time - start_time  # 计算执行时间
    print(f"It took {execution_time} seconds to execute.")
    print(f"Statistics: {cnt}")

if __name__ == '__main__':

    main()

