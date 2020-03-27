# Base template: Consists of header and footer for pages (static)
template_base = open('./templates/base.html').read()

# Page list - Includes list of different content per page, url and title
pages = [
    {
        'filename': './content/index.html',
        'output': './docs/index.html',
        'title': 'About Me'
    },
    {
        'filename': './content/resume.html',
        'output': './docs/resume.html',
        'title': 'My Resume'
    },
    {
        'filename': './content/blog.html',
        'output': './docs/blog.html',
        'title': 'My Blog'
    }
]

# Main method: Cycles through different page in pages list
def main():
    for page in pages:
        create_page(page)

# Method: creates actual page; param: dict for specific page
def create_page(page_dic):
    open(page_dic['output'], 'w+').write(assemble_page(page_dic['filename'], page_dic['title']))

# Method: combines base and content template; param: content html code
def assemble_page(middle_filename, title):
    template_middle = open(middle_filename).read()
    # print(template_middle)
    # print(template_base)
    complete_html = template_base.replace("{{content}}", template_middle)
    complete_html = complete_html.replace("{{title}}", title)
    return complete_html

main()
