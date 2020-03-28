# Base template: Consists of header and footer for pages (static)
template_base = open('./templates/base.html').read()

# Page list - Includes list of different content per page, url and title
pages = [
    {
        'filename': './content/index.html',
        'output': './docs/index.html',
        'title': 'About Me',
        'page': 'index',
        'navbar': [
            {'navbar_index_disable': ' disabled'},
            {'navbar_resume_disable': ''},
            {'navbar_blog_disable': ''}
        ]
    },
    {
        'filename': './content/resume.html',
        'output': './docs/resume.html',
        'title': 'My Resume',
        'page': 'resume',
        'navbar': [
            {'navbar_index_disable': ''},
            {'navbar_resume_disable': ' disabled'},
            {'navbar_blog_disable': ''}
        ]
    },
    {
        'filename': './content/blog.html',
        'output': './docs/blog.html',
        'title': 'My Blog',
        'page': 'blog',
        'navbar': [
            {'navbar_index_disable': ''},
            {'navbar_resume_disable': ''},
            {'navbar_blog_disable': ' disabled'}
        ]
    }
]

page_types = ['index', 'resume', 'blog']

# Main method: Cycles through different page in pages list
def main():
    for page in pages:
        create_page(page)
    print('Pages Built Successfully!!!!')

# Method: creates actual page; param: dict for specific page
def create_page(page_dict):
    open(page_dict['output'], 'w+').write(assemble_page(page_dict))

# Method: combines base and content template; param: content html code
def assemble_page(page_dict):
    template_middle = open(page_dict['filename']).read()
    complete_html = template_base.replace("{{content}}", template_middle)
    complete_html = complete_html.replace("{{title}}", page_dict['title'])
    complete_html = set_disable_navbar(page_dict, complete_html)
    return complete_html

def set_disable_navbar(page_dict, complete_html):
    navbar_lists = page_dict['navbar']
    for page_type in page_types:
        dict_key_value = 'navbar_' + page_type + '_disable'
        new_replace = '{{' + dict_key_value + '}}'
        for dict_item in navbar_lists:
            if dict_key_value in dict_item:
                complete_html = complete_html.replace(new_replace, dict_item[dict_key_value])
    return complete_html

main()
