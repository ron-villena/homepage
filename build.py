# Base template: Consists of header and footer for pages (static)
template_base = open('./templates/base.html').read()

# Page list - Includes list of different content per page, url, title & control settings
pages = [
    {
        'filename': './content/index.html',
        'output': './docs/index.html',
        'title': 'About Me',
        'page': 'index',
        'navbar': [
            {'navbar_index_action': ' disabled'},
            {'navbar_resume_action': ''},
            {'navbar_blog_action': ''}
        ],
        'carousel': [
            {'carousel_index_action': ' active'},
            {'carousel_resume_action': ''},
            {'carousel_blog_action': ''}
        ],
        'carousel_link': [
            {'carousel_link_index_action': '#bottom'},
            {'carousel_link_resume_action': './resume.html'},
            {'carousel_link_blog_action': './blog.html'}
        ],
        'carousel_link_verbiage': [
            {'carousel_link_verbiage_index_action': 'Show Me More'},
            {'carousel_link_verbiage_resume_action': 'Show Me'},
            {'carousel_link_verbiage_blog_action': 'Show Me'}
        ]
    },
    {
        'filename': './content/resume.html',
        'output': './docs/resume.html',
        'title': 'My Resume',
        'page': 'resume',
        'navbar': [
            {'navbar_index_action': ''},
            {'navbar_resume_action': ' disabled'},
            {'navbar_blog_action': ''}
        ],
        'carousel': [
            {'carousel_index_action': ''},
            {'carousel_resume_action': ' active'},
            {'carousel_blog_action': ''}
        ],
        'carousel_link': [
            {'carousel_link_index_action': './index.html'},
            {'carousel_link_resume_action': '#bottom'},
            {'carousel_link_blog_action': './blog.html'}
        ],
        'carousel_link_verbiage': [
            {'carousel_link_verbiage_index_action': 'Show Me'},
            {'carousel_link_verbiage_resume_action': 'Show Me More'},
            {'carousel_link_verbiage_blog_action': 'Show Me'}
        ]
    },
    {
        'filename': './content/blog.html',
        'output': './docs/blog.html',
        'title': 'My Blog',
        'page': 'blog',
        'navbar': [
            {'navbar_index_action': ''},
            {'navbar_resume_action': ''},
            {'navbar_blog_action': ' disabled'}
        ],
        'carousel': [
            {'carousel_index_action': ''},
            {'carousel_resume_action': ''},
            {'carousel_blog_action': ' active'}
        ],
        'carousel_link': [
            {'carousel_link_index_action': './index.html'},
            {'carousel_link_resume_action': './resume.html'},
            {'carousel_link_blog_action': '#bottom'}
        ],
        'carousel_link_verbiage': [
            {'carousel_link_verbiage_index_action': 'Show Me'},
            {'carousel_link_verbiage_resume_action': 'Show Me'},
            {'carousel_link_verbiage_blog_action': 'Show Me More'}
        ]
    }
]

# Page Types List
page_types = ['index', 'resume', 'blog']

# Control Type List
control_types = ['navbar', 'carousel', 'carousel_link', 'carousel_link_verbiage']

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
    for control_type in control_types:
        complete_html = set_control_properties(page_dict, complete_html, control_type)
    return complete_html

# Method: sets class properties for each control in the Control Type List
#         for each page in Page Types List
def set_control_properties(page_dict, complete_html, control_type):
    navbar_lists = page_dict[control_type]
    for page_type in page_types:
        dict_key_value = control_type + '_' + page_type + '_action'
        new_replace = '{{' + dict_key_value + '}}'
        for dict_item in navbar_lists:
            if dict_key_value in dict_item:
                complete_html = complete_html.replace(new_replace, dict_item[dict_key_value])
    return complete_html

main()
