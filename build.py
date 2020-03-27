# old template
# template_top = open('./templates/template_top.html').read()
# template_bottom = open('./templates/template_bottom.html').read()

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
        'title': 'Resume'
    },
    {
        'filename': './content/blog.html',
        'output': './docs/blog.html',
        'title': 'blog'
    }
]

# Main method: Cycles through different page in pages list
def main():
    for page in pages:
        create_page(page)

# Method: creates actual page; param: dict for specific page
def create_page(page_dic):
    open(page_dic['output'], 'w+').write(assemble_page(page_dic['filename']))

# Method: combines base and content template; param: content html code
def assemble_page(middle_filename):
    template_middle = open(middle_filename).read()
    # print(template_middle)
    # print(template_base)
    complete_html = template_base.replace("{{content}}", template_middle)
    return complete_html


main()

# HW2 Code
# template_top = open('./templates/template_top.html').read()
# template_bottom = open('./templates/template_bottom.html').read()
#
# template_index = open('./content/index.html').read()
#
# # Create index.html
# index_html = template_top + template_index + template_bottom
# open('./docs/index.html', 'w+').write(index_html)
#
# template_resume = open('./content/resume.html').read()
#
# # Create resume.html
# resume_html = template_top + template_resume + template_bottom
# open('./docs/resume.html', 'w+').write(resume_html)
#
# template_blog = open('./content/blog.html').read()
#
# # Create blog.html
# blog_html = template_top + template_blog + template_bottom
# open('./docs/blog.html', 'w+').write(blog_html)
