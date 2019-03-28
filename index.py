from flask import Flask
from flask import request
import flask

import os
import time

from escher_pattern import Escher_Pattern

app = Flask(__name__)

@app.route("/")
def generate_pattern():

  # defaults
  params = {
    'LPM': 50,
    'PAGE_WIDTH': 270,
    'PAGE_HEIGHT': 210,
    'ROTATE': 5,
    'ESCHER': 2
  }

  for k,v in params.items():
    rq_param = request.args.get(k)
    if rq_param!=None:
      params[k] = float(rq_param)

  basename  = 'escher-pattern'
  basename += '-ESCHER'+str(params['ESCHER'])
  basename += '-LPM'+str(params['LPM'])
  basename += '-ROT'+str(params['ROTATE'])
  basename += '-PAGE_WIDTH'+str(params['PAGE_WIDTH'])
  basename += '-PAGE_HEIGHT'+str(params['PAGE_HEIGHT'])
  pdf_name  = basename+".pdf"

  ep = Escher_Pattern(
         width  = params['PAGE_WIDTH'],
         height = params['PAGE_HEIGHT'],
         escher = params['ESCHER'],
         lpm    = params['LPM'],
         rotate = params['ROTATE'])

  ep.generate()
  ep.save()

  with open(pdf_name,'rb') as f:
    contents = f.read()
  os.remove(pdf_name)

  filesize = str(len(contents))
  filesize = filesize.encode('utf-8')

  resp = flask.Response(contents)

  resp.headers['Content-Type']        = 'application/pdf'
  resp.headers['Cache-Control']       = 'public, must-revalidate, max-age=0'
  resp.headers['Pragma']              = 'public'
  resp.headers['Expires']             = 'Sat, 26 Jul 1997 05:00:00 GMT'
  resp.headers['Last-Modified']       = time.strftime("%a, %d %b %Y %H:%M:%S GMT", time.gmtime())
  resp.headers['Content-Length']      = str(len(contents))
  resp.headers['Content-Disposition'] = 'inline; filename='+pdf_name+';'

  return resp

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=int("5000"), debug=True)
