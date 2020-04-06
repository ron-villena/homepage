import glob
import os

# base template file path: Consists of header and footer for pages (static)
template_base = open('./templates/base.html').read()

# dir for output html files
output_dir = './docs/'

# page types list
page_types = [
    {
    'page_name': 'index',
    'carousel': {
        'carousel_header': 'WHO AM I',
        'carousel_desc': 'Husband - Father - Gentleman'
        }
    },
    {
    'page_name': 'resume',
    'carousel': {
        'carousel_header': 'MY WORK',
        'carousel_desc': 'Dedicated - Hard - Smart'
        }
    },
    {
    'page_name': 'blog',
    'carousel': {
        'carousel_header': 'MY THOUGHTS',
        'carousel_desc': 'Fun - Interesting - Perspective'
        }
    }
]

# receive arguments from manage.py and decides what needs to be done
def read_argmts(argv_list):
    if len(argv_list) > 1:
        command = argv_list[1]
        if command == 'build':
            print("Build was specified")
            create_pages_dict()
        elif command =='new':
            print("New page was specified")
            create_new_content_page()
        else:
            print_instr()
    else:
        print_instr()

# create new content page
def create_new_content_page():
    new_page_content = '''
        <h1>New Content!</h1>
        <br>
        <p>New content...</p>
    '''
    open('./content/new_content_page.html', 'w+').write(new_page_content)

# prints instructions when no argument is given when running manage.py
def print_instr():
    print_instr_text = '''
        Usage:
            Rebuild Site:       python3 manage.py build
            Create New Page:    python3 manage.py new
            Please specify "build" or "new"
    '''
    print(print_instr_text)

# the page dictionary for all html in ./content/
def create_pages_dict():
    all_html_files = glob.glob("./content/*.html")
    for file_path in all_html_files:
        file_dict = {}
        file_dict['filename'] = file_path
        # print(file_dict['filename'])
        file_name = os.path.basename(file_path)
        name_only, extension = os.path.splitext(file_name)
        file_dict['output'] = output_dir + file_name
        file_dict['title'] = name_only
        file_dict['page'] = name_only
        build_page(file_dict)

# builds each page according to page dict
def build_page(page_dict):
    from jinja2 import Template
    content_html = open(page_dict['filename']).read()
    template_html = open("./templates/base.html").read()
    template = Template(template_html)
    html_result = template.render(
        title=page_dict['title'],
        page=page_dict['page'],
        pages=page_types,
        navbar_active=' disabled',
        carousel_active=' active',
        non_active='',
        bottom_link='#bottom',
        content=content_html,
    )
    open(page_dict['output'], 'w+').write(html_result)
