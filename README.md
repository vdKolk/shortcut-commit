# shortcut-commit
Commit in a "correct" format using Shortcut story number and title

### usage:
first run setup
```shell
    ./setup.py
```
after entering the shortcut key, the script is ready for use

### running:
In the project dir that you want to commit run
```shell
    ./{{path-to-files}}/commit.py
```

Or if you want to amend to a commit run
```shell
    ./{{path-to-files}}/commit.py -a
```

### Alias
```
alias scc='../../vdKolk/shortcut-commit/commit.py'
alias scca='scc -a'

function branch {
    git checkout -B feature-ops/sc-"$1" upstream/main
    git stash
    git pull upstream main
    git stash pop
}

function checkout {
    git checkout feature-ops/sc-"$1"
}
```
