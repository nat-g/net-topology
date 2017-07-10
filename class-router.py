class Router(object):
	"""This is a class that describes a Router"""
	def __init__(self, routername, model, serialno, ios):
		super(Router, self).__init__()
		self.routername = routername
		self.model = model
		self.serialno = serialno
		self.ios = ios

	def PrintRouter(self, manuf_date):
		print "The router name is: ", self.routername
		print "The router model is: ", self.model
		print "The router serial number is: ", self.serialno
		print "IOS version is: ", self.ios
		print "Model and manufactured date combined is: ", self.model + manuf_date
		
		