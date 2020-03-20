template_top = open('./templates/template_top.html').read()
template_bottom = open('./templates/template_bottom.html').read()

template_index = open('./content/index.html').read()

# Create index.html
index_html = template_top + template_index + template_bottom
open('./docs/index.html', 'w+').write(index_html)

template_resume = open('./content/resume.html').read()

# Create resume.html
resume_html = template_top + template_resume + template_bottom
open('./docs/resume.html', 'w+').write(resume_html)

template_blog = open('./content/blog.html').read()

# Create blog.html
blog_html = template_top + template_blog + template_bottom
open('./docs/blog.html', 'w+').write(blog_html)
