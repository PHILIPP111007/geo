#!/bin/bash

venv=""
migrations=""
superuser=""
static=""

read -p "[1 / 4] Create venv and download packages? [y / n] : " venv
read -p "[2 / 4] Create migrations? [y / n] : " migrations
read -p "[3 / 4] Create superuser? [y / n] : " superuser
read -p "[4 / 4] Collect static files? [y / n] : " static

# `tmp` directory is for gunicorn.pid file
make_tmp() {
	mkdir $PWD/tmp
}

create_venv() {
	if [ ! -d "venv" ]
		then
			python3 -m venv venv
	fi

	source $PWD/venv/bin/activate
	pip install --upgrade pip

	if [ -f "requirements.in" ]
		then
			pip install -r requirements.in
			pip freeze > requirements.txt
		else
			if [ -f "requirements.txt" ]
				then
					pip install -r requirements.txt
				else
					echo "Venv script: requirements file does not exist."
			fi
	fi

	pip list
	echo "Venv script: venv created."
}

create_migrations() {
	if [ -d "venv" ]
		then
			source $PWD/venv/bin/activate
			python manage.py makemigrations
			python manage.py migrate
			echo "Migrations script: migrations created."
		else
			echo "Migrations script: you dont have venv."
	fi
}

create_superuser() {
	if [ -d "venv" ]
		then
			source $PWD/venv/bin/activate
			python manage.py createsuperuser
		else
			echo "Migrations script: you dont have venv."
	fi
}

collect_static() {
	if [ -d "venv" ]
		then
			source $PWD/venv/bin/activate
			python manage.py collectstatic
		else
			echo "Static script: you dont have venv."
	fi
}

if [ ! -d "tmp" ]
	then
		make_tmp
fi

# Create venv and install packages
if [ $venv = "y" ]
	then
		create_venv
fi

# Make migrations
if [ $migrations = "y" ]
	then
		create_migrations
fi

# Create super user
if [ $superuser = "y" ]
	then
		create_superuser
fi

# Collect static files
if [ $static = "y" ]
	then
		collect_static
fi

echo "Main script: Done."