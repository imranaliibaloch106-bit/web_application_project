from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']
        return f"Thank you {name}! Your message has been received."
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        father_name = request.form['father_name']
        phone = request.form['phone']
        address = request.form['address']
        city = request.form['city']
        country = request.form['country']
        message = request.form['message']

        return f"""
        <h2>Thank you {name}!</h2>
        <p>We have received your message.</p>
        <p><b>Father Name:</b> {father_name}</p>
        <p><b>Phone:</b> {phone}</p>
        <p><b>Address:</b> {address}, {city}, {country}</p>
        <p><b>Your Message:</b> {message}</p>
        <br><a href='/'>Back to Home</a>
        """
    return render_template('contact.html')
