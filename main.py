from flask import Flask, render_template, request, redirect, flash
import json, person

app = Flask(__name__)

app.secret_key = 'mysecretkey'

data = { 'clients': [] }

@app.route('/')
def index():
	return render_template('index.html', data=data['clients'])

@app.route('/add', methods=['POST'])
def add_contact():
	client = person.Client(len(data['clients']))
	client._fullname = request.form['fullname']
	client._phone = request.form['phone']
	client._email = request.form['email']
	data['clients'].append(client)
	json_data = json.dumps(data, indent=4, cls=person.ClientEncoder)
	with open('./data.json', 'w') as file:
		json.dump(json.loads(json_data), file, indent=4)

	flash('Client added successfully')
	return redirect('/')

@app.route('/edit/<string:id>')
def edit(id):
	return render_template('edit.html', data=data['clients'][int(id)])

@app.route('/update/<string:id>', methods=['POST'])
def update(id):
	data[id]._fullname = request.form['fullname']
	data[id]._phone = request.form['phone']
	data[id]._email = request.form['email']
	flash('Client updated successfully')
	return redirect('/')

@app.route('/delete/<string:id>')
def delete(id):
	json_data = str(json.load(open('./static/json/data.json')))
	print(json_data)
	for row in range(len(json_data)):
		if json_data[row]['_id'] == id:
			json_data.pop(row)

	flash('Client removed successfully')
	return redirect('/')

if __name__=='__main__':
	app.run(debug=True, port=5000)