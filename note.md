## Local 
```
bundle exec jekyll serve --livereload
```
```
bundle exec jekyll serve --livereload --port 8000 --config _config.lamda.yml              
```

## Deploy on Github

First commit and push to github master branch.

Use the default `_config.yml` to build and deploy the site:
```
./bin/deploy
```
This command will generate site files from master branch to gh-pages branch and push.

Github action is not yet set.

## Deploy on LAMDA server
Deploy on LAMDA server require domestic CDN and different url setting. Thus we use a `_config.lamda.yml`.

To build:
```
bundle exec jekyll build --config _config.lamda.yml
```
This command generate files to _site directory.

To push:
```
scp -r _site/* xiez@www.lamda.nju.edu.cn:d:/personal_web/xiez
```