from jinja2 import Environment, FileSystemLoader

description = 'asdasd asd a sd asd'
scrore = '100'

with open('Margaux1.html', 'w') as file:
    file_loader = FileSystemLoader('')
    env = Environment(loader=file_loader)
    tm = env.get_template('tamplate.html')
    msg = tm.render(name=name, descriprion_=description, score_=scrore)
    file.write(msg)
    file.close()