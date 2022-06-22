import argparse
import os


def get_py_template(prob_num):
    return f"""\n\
# https://www.acmicpc.net/problem/{prob_num}
def sol_{prob_num}():
    pass

def other_{prob_num}():
    pass
\n\n
"""

def get_js_template(prob_num):
    return f"""\n
const sol_{prob_num} = () => {{
    console.log("Hello World!");
}}

const other_{prob_num} = () => {{
    console.log("Hello World!");
}}
\n\n"""

first_line = {
    "python": """\nproblems = [HERE]
    """
}
get_template = {"python": get_py_template, "js": get_js_template}

def make_template(file_path, template, problems):
    if not problems:
        return
    
    with open(file_path, "a") as f:
        f.write(first_line["python"].replace('HERE', ", ".join(map(str, problems))))
        for p_num in problems:
            f.write(template(prob_num=p_num))



"""
사용예
python make_script_file.py --name binarysearch -p 1654 2512 10816

"""

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Make new python file with 1 line.')
    parser.add_argument('--lang', metavar='Lang', type=str, default='python',
                        help='Programming Languague to use')
    parser.add_argument('--dir', default='algorithms',
                        help='Type directory name, then new script file will be there.')
    parser.add_argument('--name', metavar='N', required=True,
                        help='Type File name, then it will be the name of the new script file.')
    parser.add_argument('-p', metavar="Problems", default=[], nargs="+", type=int)

    args = parser.parse_args()
    print(args)
    def get_ext(key):
        return {"python": "py", "js": "js", "swift": "swift"}.get(key, False)
    lang = args.lang
    ext = get_ext(lang)
    if ext:
        path = f'{os.getcwd()}/{lang}/{args.dir}/{args.name}.{ext}'
        make_template(path, get_template[lang], args.p)
    pass

