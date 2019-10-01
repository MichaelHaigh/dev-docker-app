from flask import Flask
from flask import render_template
import os
import subprocess

app = Flask(__name__)

POSTGRES = {
    'user': 'postgres',
    'pw': 'password',
    'db': 'my_database',
    'host': 'localhost',
    'port': '5432',
}

app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

def is_docker():
    path = '/proc/self/cgroup'
    return (
        os.path.exists('/.dockerenv') or
        os.path.isfile(path) and any('docker' in line for line in open(path))
    )

def is_aws():
    command = ["sudo", "dmidecode"]
    return (any('Xen' in line for line in subprocess.check_output(command).split('\n')))

@app.route("/")
def main():
    message = "Hello 1-Click K8S CI/CD!"

    if is_docker():
        runningon = "karbon.png"
        builtby   = "jenkins.png"

    elif is_aws():
        runningon = "amazon.png"
        builtby   = "calm.png"

    else:
        runningon = "ahv.png"
        builtby   = "calm.png"

    hostname = os.uname()[1]

    return render_template('index.html', message=message, hostname=hostname,
                           runningon=runningon, builtby=builtby)

if __name__ == '__main__':
    app.run(host = '0.0.0.0')
