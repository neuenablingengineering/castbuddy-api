from app import app
from app import pusher
from flask import render_template, flash, redirect, request, abort, jsonify
from app.forms import LoginForm

logged_in = False

class Packet:
    def __init__(self, id, timestamp, value):
        self.id = id
        self.timestamp = timestamp
        self.value = value

# Hologram webhook
@app.route('/api/holohook', methods=['POST', 'GET'])
def holohook():
    if request.method == 'POST':
        from app.database import db, DataEntry

        msg = request.get_json()
        print(msg)
        data = msg['d']
        device = msg['c']
        for entry in data :
            newDataEntry = DataEntry( chip_id=device,\
                timestamp=entry['t'], \
                s0=entry['v'][0], \
                s1=entry['v'][1], \
                s2=entry['v'][2], \
                s3=entry['v'][3], \
                s4=entry['v'][4], \
                s5=entry['v'][5], \
                s6=entry['v'][6], \
                s7=entry['v'][7], \
                s8=entry['v'][8], \
                s9=entry['v'][9], \
                s10=entry['v'][10], \
                s11=entry['v'][11], \
                s12=entry['v'][12], \
                s13=entry['v'][13], \
                s14=entry['v'][14], \
                s15=entry['v'][15])
            db.session.add(newDataEntry)
            db.session.commit()
        return '', 200
    else:
        abort(400)

@app.route('/api/chip/select/all')
def chipSelectTest():
    from app.database import Chip
    return jsonify([repr(o) for o in Chip.query.all()])

# Get range of entries
@app.route('/api/data/select')
def dataSelect():
    from app.database import DataEntry
    chip = request.args['chip']
    start = request.args['start']
    end = request.args['end']
    recs = DataEntry.query.filter(DataEntry.chip_id==chip, DataEntry.timestamp >= start, DataEntry.timestamp <= end)
    return jsonify([o.toDict() for o in recs])

# Get all entries
@app.route('/api/data/select/all')
def dataSelectTest():
    from app.database import DataEntry
    return jsonify([repr(o) for o in DataEntry.query.all()])

# Manual data insertion
@app.route('/api/data/inserttest', methods=['GET', 'POST'])
def holohookInsertTest():
    import datetime
    from app.database import db, DataEntry
    from random import randint
    ts = str(datetime.datetime.utcnow())
    chip_id = 'NOT_CONNECTED_YET'
    testData = DataEntry(chip_id=chip_id, timestamp=ts, sensors=(randint(0, 255) for i in range(16)))
    db.session.add(testData)
    db.session.commit()
    return jsonify(repr(testData))

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home', logged_out=not logged_in)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print("VALID FORM")
        flash('Logging in to your account, {}'.format(form.username.data))
        return redirect('/index')
    else:
        print("Form Not Valid")
    return render_template('login.html', title='Log In', form=form)

@app.route('/data')
def data():
    from os import listdir, getcwd
    from os.path import isfile, join
    import json

    data = []

    my_path = getcwd() + "/app/data"
    file_names = [f for f in listdir(my_path) if isfile(join(my_path, f))]

    for f_name in file_names:
        split_name = f_name.split('__')
        p_id = split_name[0]
        p_ts = split_name[1].split('.')[0] # get rid of the '.txt' at the end of the name
        with open(join(my_path, f_name)) as f:
            jo = json.loads(f.read())
            data.append(Packet(p_id, p_ts, jo['t']))

    return render_template('data.html', title='Data', data_list=data)

"""
@app.route('/test/chip/insert', methods=['GET', 'POST'])
def insertChipTest():
    import random
    from app.database import db, Chip
    from flask import jsonify
    testChipName = "TEST_CHIP_%04d" % random.randint(0, 9999)
    testChip = Chip(chip_name=testChipName)
    db.session.add(testChip)
    db.session.commit()
    return jsonify(repr(testChip))
"""
