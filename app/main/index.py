from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask import current_app as app
# 추가할 모듈이 있다면 추가
 
main= Blueprint('main', __name__, url_prefix='/')

@main.route('/',methods=['GET'])
def base():
	return render_template('base.html')
 
@main.route('/main', methods=['GET'])
def mainscreen():
	return render_template('main.html')

@main.route('/About', methods=['GET'])
def about():
	return render_template('about.html')
