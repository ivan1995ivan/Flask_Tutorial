from jinja2 import Template

data = '''{% raw %}Модуль Jinja вместо
определения {{ name }} 
подставляет соответвующее значение{% endraw %}'''

tm = Template(data)
msg = tm.render(name='Федор')

print(msg)