const Nexmo = require('nexmo');

const recipient_number = ; //Recipients number here
var message = 'This is a test message to check for nodejs messaging';


function send_admin_sms(recipient_number,message)
{
	const nexmo = new Nexmo(
		{ apiKey: 'YOUR_API_KEY',
  		  apiSecret: 'YOUR_SECRET_KEY'
		},	
		 {debug: true}
		);


		nexmo.message.sendSms('FromMedicento', recipient_number, message, { type: 'unicode' },
    	(err, responseData) => {
      		if(err) {
        		console.log(err);
      		}
       		else {
        		console.dir(responseData);
       			 // Get data from response
        		const data = {
          		id: responseData.messages[0]['message-id'],
          		number: responseData.messages[0]['to']
       			}


      			}	
    							}
  		);

}

send_admin_sms(recipient_number,message)