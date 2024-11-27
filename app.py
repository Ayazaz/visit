from flask import Flask, render_template, request
from forms import VisaForm
from visa_requirements import check_eligibility

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

@app.route('/', methods=['GET', 'POST'])
def index():
    form = VisaForm()
    if form.validate_on_submit():
        user_data = {
            'name': form.name.data,
            'age': form.age.data,
            'education': form.education.data,
            'experience': form.experience.data,
            'language': form.language.data,
            'country': form.country.data,
        }
        result = check_eligibility(user_data)
        return render_template('results.html', result=result, user=user_data)
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
