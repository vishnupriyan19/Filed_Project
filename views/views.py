from flask import Blueprint, request, abort, jsonify
import json
from application.services.payment import Card, PaymentGateway

blueprint = Blueprint("views", __name__, url_prefix="/")


@blueprint.route("/ProcessPayment", methods=['POST' , 'GET'])
def payment():

	if request.method == 'POST':
	  data = request.get_data(as_text=True)
	  if not data:
			abort(400)
		request_data = json.loads(data)
		card_data = Card()
		print("request data {}".format(request_data))
		try:
			if not card_data.verify_input(**request_data):
				print("card data invalid")
				abort(400)
		except:
			abort(400)
		try:
			payment_status = PaymentGateway(card_data.Amount, card_data)
			print("payment process started")
			payment_success= payment_status.make_payment()
			
			if payment_success:
				return {"status code": 200}, 200
			else:
				abort(400)
		except:
			abort(500)
	else:
		abort(400)
