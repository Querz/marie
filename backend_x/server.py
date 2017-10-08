import json
import datetime
import tornado.ioloop
import tornado.web


class BackendResponse(object):

	data = {}

	def __init__(self, data=None):
		if data:
			self.data.update(data)

	def json(self):
		self.data['time'] = datetime.datetime.now().__str__()
		return json.dumps(self.data)


class MainHandler(tornado.web.RequestHandler):

	def set_custom_headers(self):
		self.set_header("Access-Control-Allow-Origin", "*")
		self.set_header("Access-Control-Allow-Headers", "x-requested-with")
		self.set_header("Content-Type", "application/json")
		self.set_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")

	def post(self):
		request_data = None
		self.set_custom_headers()

		try:
			data = self.request.body

			if data and isinstance(data, dict) \
				or data and isinstance(data, list):

				request_data = json.loads(data)

		except Exception, e:
			log_exception(e)

		resp = BackendResponse().json()
		log_request(data, resp, 'post-request')

		self.write(resp)

	def get(self):
		self.set_custom_headers()

		request_data = self.request.arguments

		resp = BackendResponse().json()
		log_request(request_data, resp, 'get-request')

		self.write(resp)


def make_app():
	return tornado.web.Application([
		(r"/", MainHandler),
	])


def log(msg, log_type):
	now = datetime.datetime.now()
	print "EventLog %s :: %s\t%s" % (now, log_type, msg)


def log_request(req, resp, rtype=None):
	log_msg = "%s\nResponse: %s" % (req, resp)
	log(log_msg, rtype)


def log_exception(e):
	log(e.message, "exception")


if __name__ == "__main__":
	app = make_app()
	app.listen(9999)
	tornado.ioloop.IOLoop.current().start()
