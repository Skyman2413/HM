from flask import render_template, redirect, send_file

from app import app, excel
from app.forms import InfoForm


@app.route('/', methods=['GET', 'POST'])
def index():
    form = InfoForm()
    if form.validate_on_submit():
        data = {
            "ФИО": f'{form.name.data} {form.lname.data} {form.mname.data}',
            "Исполнитель": f'{form.executor_name.data}',
            "Услуга": f'{form.service_name.data}',
            "Дата Выставления": f'{form.date.data}'
        }
        excel.form_file(data)
        redirect('download')
    return render_template('form.html', form=form)


@app.route('/download')
def download():
    path = "/test.xlsx"
    return send_file(path, as_attachment=True)