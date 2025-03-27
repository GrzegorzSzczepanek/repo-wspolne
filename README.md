```
  275  neofetch
  276  git clone git@github.com:GrzegorzSzczepanek/repo-wspolne.git
  277  git clone git@github.com:GrzegorzSzczepanek/indywidulane-repo.git
  278  ls
  279  mkdir lab3
  280  mv indywidulane-repo/ repo-wspolne/
  281  mv repo-wspolne/ lab3/
  282  cd lab3
  283  ls
  284  nv
  285  nvim
  286  ls
  287  cd repo-wspolne/
  288  git pull
  289  nvim
  290  ls
  291  nv index.rst
  292  nvim index.rst
  293  ls
  294  nvim index.rst
  295  git status
  296  git add .
  297  mv indywidulane-repo/ ..
  298  git status
  299  git add .
  300  git commit -m "index rst setup"
  301  mc
  302  cd ../indywidulane-repo/
  303  cd ..
  304  ls
  305  cd repo-wspolne/
  306  git status
  307  git push
  308  ls
  309  vim README.md
  310  git add .
  311  git status
  312  git commit -m "fix"
  313  git config --global --edit
  314  cat ~/.gitconfig
  315  git commit --amend --reset-author
  316  git push
  317  cd ../indywidulane-repo/
  318  poetry init
  319  ls
  320  ls ..
  321  nvim
  322  poetry env use
  323  poetry env use /home/student20/.pyenv/versions/3.12.9/bin/python
  324  poetry add sphinx
  325  poetry run
  326  poetry run sphinx-quickstart
  327  mc
  328  nvim .gitignore
  329  git status
  330  git add .
  331  git commit -m "sphinx setup"
  332  git push
  333  mc
  334  git submodule add git@github.com:GrzegorzSzczepanek/repo-wspolne.git source/przeglad/monitorowanie
  335  git status
  336  git add .
  337  git commit -m "monitorowanie"
  338  git push
  339  mc
  340  nvim
  341  poetry run make html
  342  poetry run make pdflatex
  343  poetry run make latexpdf
  344  git status
  345  history
