#eb-virtcreate virtual env  for python the name is eb-virt
python3 -m venv eb-virt
# to active virtual env eb-virt:
source eb-virt/bin/activate
#insatall  all lib with pip
#create your project and run it
#when you installed all what you need freeze in  requirements.txt within pip
pip freeze > requirements.txt
#install heroku 
brew install heroku/brew/heroku
#login tu your heroku account 
heroku login
#create heroku project for example stm-django 
heroku create stm-django
heroku git:remote -a stm-django
#install gunicorn
pip install gunicorn
#setup witch programme to run, in our case in the directory we have wsgi python is ebdjango
gunicorn ebdjango.wsgi
# to run heroku locally
heroku local
#create Procfile in it insert:
web: gunicorn ebdjango.wsgi --preload

# add  Procfile to git, commit and push all to heroku server
git add .
git commit -m 'add Procfile'
git push heroko master
#to test your app
heroku open
#if any lib missing in your heroko you can installed in this way:
#create file Aptfile with missing lib in my case
libsm6
libxrender1
libfontconfig1
libice6
tesseract-ocr
tesseract-ocr-eng

#create buildpack for heroku
heroku create --buildpack https://github.com/paulfurley/heroku-buildpack-python-opencv-3.1.0.git
heroku create --buildpack https://github.com/matteotiziano/heroku-buildpack-tesseract.git
heroku buildpacks:add --index 1 heroku-community/apt
heroku run bash
heroku config:set TESSDATA_PREFIX=./.apt/usr/share/tesseract-ocr/4.00/tessdata
git add . 
git commit -m 'change settings '
git push heroku master
#  test all 
heroku open
#if the app don't find file in templates directory you have to change in setting file in this way:
fpages is the directory where templates directory is installed 
'DIRS': [ os.path.join(BASE_DIR, 'fpages/templates')]

