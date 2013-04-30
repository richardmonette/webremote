import os, subprocess, signal

from flask import Flask, render_template, session, request

app = Flask(__name__)
app.secret_key = 'mainsession'

@app.route('/play/', methods=['POST'])
def play():
	cmds = ['omxplayer', '-o', 'hdmi', '/mnt/ntserver/%s' % str(request.form['filename'])]
	session['process'] = subprocess.Popen(cmds)
	print cmds
	return 'Starting...'

@app.route('/stop/', methods=['POST'])
def stop():
	session['process'].kill()
	return 'Stopping...'

@app.route('/')
def index():
	mp4filenames = [filename for filename in os.listdir('/mnt/ntserver') if 'mp4' in filename]
	return render_template('index.html', filenames=mp4filenames)

if __name__ == '__main__':
	app.run(host='0.0.0.0',debug=True)
