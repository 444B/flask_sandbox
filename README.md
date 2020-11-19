
TODO:
configure launcher.sh to automate all the steps below

STEPS: :arrow_heading_down:

:one: : DOWNLOAD 

	git clone https://github.com/444B/flask_sandbox.git
:two: : ACTIVATE

	cd <dir/of/cloned/repo>
	source virtual/bin/activate
:three: : RUN

	export FLASK_APP=app.py
	export FLASK_ENV=development
	flask run
	
To DEACTIVATE VENV:

	deactivate

