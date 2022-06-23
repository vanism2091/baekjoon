import argparse
import os
from re import template
import prob_parser
from prob_templates import get_js_template, get_py_template, first_line, get_readme_template


get_template = {"python": get_py_template, "js": get_js_template}

"""
사용예
js file
python make_script_file.py --lang js --dir step --name step9


python file
python make_script_file.py --dir step --name step10
python make_script_file.py --name dynamicprogramming -p 9655 1463 1003 2579 9461 2193 14501

js file
python make_script_file.py --lang swift --dir step --name step2
"""

"""
문제별로 파일을 나누는게 좋겠다.. :)

python make_script_file.py --name graph -p 1012 1260 1697 2178 2468 2667 7576 10026
python make_script_file.py --name binarysearch -p 1654 2512 2805 10816
"""


# 파일 안에 문제 다 때려넣는 템플릿
def make_template(file_path, template, problems):
    if not problems:
        return
    
    with open(file_path, "a") as f:
        f.write(first_line["python"].replace('HERE', ", ".join(map(str, problems))))
        for p_num in problems:
            f.write(template(prob_num=p_num))



# 문제별로 파일을 새로 만드는 템플릿
def make_template_2(file_path, template, problems, title):
    if not problems:
        return
    # README가 없다면 README.md를 만든다
    try:
        if not os.path.exists(file_path):
            os.makedirs(file_path)
    except OSError:
        print('Error: Creating directory. '+ file_path)
    with open(f'{file_path}/README.md', "a+") as rmf:
        rmf.seek(0)
        lines = rmf.readlines()
        if not lines:
            rmf.write(get_readme_template(title=title, isInit=True))
            last_idx = 0
        else:
            last_idx = int(lines[-1][1:8])

        for i, p_num in enumerate(problems):
            # 이미 {p_num.py}가 있으면 continue
            if os.path.isfile(f'{file_path}/{p_num}.py'):
                print(f'{p_num}.py already exists.')
                continue

            # level, prob_title을 받아온다
            level, prob_title = prob_parser.parse_probs_info(p_num)
            
            # README.md를 수정한다
            last_idx += 1
            rm_data = {
                "keys":     ["index", "prob_num", "title", "level"],
                "values":   [last_idx, p_num, prob_title, level]
            }
            rm_args = {k:v for k, v in zip(rm_data["keys"], rm_data["values"])}
            rmf.write(get_readme_template(**rm_args))
            
            # {p_num}.py를 만든다
            with open(f'{file_path}/{p_num}.py', "a") as f:
                f.write(template(prob_num=p_num, title=prob_title))




if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Make new python file with 1 line.')
    parser.add_argument('--lang', metavar='Lang', type=str, default='python',
                        help='Programming Languague to use')
    parser.add_argument('--dir', default='algorithms',
                        help='Type directory name, then new script file will be there.')
    # parser.add_argument('--name', metavar='N', required=True,
    parser.add_argument('--name', metavar='N', default="",
                        help='Type File name, then it will be the name of the new script file.')
    parser.add_argument('-p', metavar="Problems", default=[], nargs="+", type=int)
    parser.add_argument('--test', metavar="onTest", default=False, type=bool)


    args = parser.parse_args()
    print(args)
    if args.test:
        print("test")
        prob_parser.test()
    else:
        print("not_test")
        def get_ext(key):
            return {"python": "py", "js": "js", "swift": "swift"}.get(key, False)
        lang = args.lang
        ext = get_ext(lang)
        # {algs}.py 하던 방식
        # if ext:
        #     path = f'{os.getcwd()}/{lang}/{args.dir}/{args.name}.{ext}'
        #     make_template(path, get_template[lang], args.p)
        if ext:
            path = f'{os.getcwd()}/{lang}/{args.dir}/{args.name}'
            print(path)
            make_template_2(file_path=path, template=get_template[lang], problems=args.p, title=args.name)
        pass

