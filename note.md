## Local 
```
bundle exec jekyll serve --livereload
```
```
bundle exec jekyll serve --livereload --port 8000 --config _config.lamda.yml              
```

## Deploy on Github

Normally if you push to master branch, the site will be automatically built and deployed to gh-pages branch.

If xie-zheng.cn 404 check github repo settings / pages / custom domain.

<!-- First commit and push to github master branch.

Use the default `_config.yml` to build and deploy the site:
```
./bin/deploy
```
This command will generate site files from master branch to gh-pages branch and push.

Github action is not yet set.

Homepage will be available at https://tedxz.github.io/

If xie-zheng.cn 404 check github pages setting. -->

<!-- 
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
or
```
scp -r _site/* lamda_server:d:/personal_web/xiez
```
(See ssh config)


Auto redirect to github page:
scp ../index.html lamda_server:d:/personal_web/xiez

Password: see keychain 210.28.132.69 (xiez) 
-->