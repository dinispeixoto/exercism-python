# paiv's solution

import re

def parse(markdown):
    markdown = re.sub(r'__([^\n]+?)__', r'<strong>\1</strong>', markdown)
    markdown = re.sub(r'_([^\n]+?)_', r'<em>\1</em>', markdown)
    markdown = re.sub(r'^\* (.*?$)', r'<li>\1</li>', markdown, flags=re.M)
    markdown = re.sub(r'(<li>.*</li>)', r'<ul>\1</ul>', markdown, flags=re.S)
    for i in range(6, 0, -1):
        markdown = re.sub(r'^{} (.*?$)'.format('#' * i), r'<h{0}>\1</h{0}>'.format(i), markdown, flags=re.M)
    markdown = re.sub(r'^(?!<[hlu])(.*?$)', r'<p>\1</p>', markdown, flags=re.M)
    markdown = re.sub(r'\n', '', markdown)
    return markdown
