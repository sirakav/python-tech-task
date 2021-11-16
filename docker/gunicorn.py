# Standart library
import multiprocessing  # noqa: F401

# ===============================================
#           Server Socket
# ===============================================

# bind - The server socket to bind
bind = "0.0.0.0:8000"

# backlog - The maximum number of pending connections
# Generally in range 64-2048
backlog = 2048

# ===============================================
#           Worker Processes
# ===============================================

# workers - The number of worker processes for handling requests.
# A positive integer generally in the 2-4 x $(NUM_CORES) range
workers = 4

# worker_class - The type of workers to use
# A string referring to one of the following bundled classes:
# 1. sync
# 2. eventlet - Requires eventlet >= 0.9.7
# 3. gevent - Requires gevent >= 0.13
# 4. tornado - Requires tornado >= 0.2
# 5. gthread - Python 2 requires the futures package to be installed (or
# install it via pip install gunicorn[gthread])
# 6. uvicorn - uvicorn.workers.UvicornWorker
#
# You’ll want to read http://docs.gunicorn.org/en/latest/design.html
# for information on when you might want to choose one of the other
# worker classes.
# See also: https://www.uvicorn.org/deployment/
worker_class = "sync"  # <- For kubernetes


# ===============================================
#           Security
# ===============================================

# limit_request_line - The maximum size of HTTP request line in bytes
# Value is a number from 0 (unlimited) to 8190.
# This parameter can be used to prevent any DDOS attack.
limit_request_line = 1024

# limit_request_fields - Limit the number of HTTP headers fields in a request
# This parameter is used to limit the number of headers in a request to
# prevent DDOS attack. Used with the limit_request_field_size it allows
# more safety.
# By default this value is 100 and can’t be larger than 32768.
limit_request_fields = 100

# limit_request_field_size - Limit the allowed size of an HTTP request
# header field.
# Value is a number from 0 (unlimited) to 8190.
limit_request_field_size = 1024


# ===============================================
#           Server Mechanics
# ===============================================

user = "app"
group = "app"

# ===============================================
#           Logging
# ===============================================

# accesslog - The Access log file to write to.
# “-” means log to stdout.
accesslog = "-"

# errorlog - The Error log file to write to.
# “-” means log to stderr.
errorlog = "-"

# ===============================================
#           Monitoring
# ===============================================
statsd_host = "localhost:9125"
statsd_prefix = "example-api"
