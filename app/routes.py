import io

from flask import render_template, redirect, send_file, make_response

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
        return redirect('/download')
    return render_template('form.html', form=form)


@app.route('/download')
def download():
    fp = open("test.xlsx", 'rb')
    bytes = fp.read()
    fp.close()
    return send_file(io.BytesIO(bytes), as_attachment=True, attachment_filename='test.xlsx')