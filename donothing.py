from pprint import pp
import mistune
import mistune.renderers
import mistune.renderers.markdown

with open("readme.md") as f:
    markdown = mistune.create_markdown(renderer='ast')
    source_text = f.read()
    ast = markdown(source_text)

assert isinstance(ast, list)

n = len(ast)
i = 0
s = []
steps = []
while i < n:
    if ast[i]['type'] != 'heading':
        s.append(ast[i])
    else:
        steps.append(s)
        s = [ast[i]]
    i += 1
steps.append(s)

renderer = mistune.renderers.markdown.MarkdownRenderer()
for step in steps:
    pp(renderer(step, mistune.core.BlockState()))
    input()

