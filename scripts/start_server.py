# -*- coding: utf-8 -*-
import sys
import os

if os.path.isdir('portfolio_monitor'):
    sys.path.append(os.path.abspath('.'))
elif os.path.isdir('../portfolio_monitor'):
    sys.path.append(os.path.abspath('..'))

from portfolio_monitor import server

def main():
    if len(sys.argv) > 1 and sys.argv[1] == '--debug':
        server.runServer(debug=True)
    else:
        server.runServer()


if __name__ == "__main__":
    main()
