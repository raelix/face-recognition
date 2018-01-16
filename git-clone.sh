git clone https://me@bitbucket.org/me/test.git
cd test
cp -R ../dummy/* .
git add .
git pull origin master 
git commit . -m "my first git commit" 
git config --global push.default simple
git push
