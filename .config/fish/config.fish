if status is-interactive
    # Commands to run in interactive sessions can go here
end

set -x GOPATH $HOME/.go
set -x GOROOT /usr/local/go
set -x PATH $PATH $GOROOT/bin $GOPATH/bin