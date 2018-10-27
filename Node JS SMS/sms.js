const Nexmo = require('nexmo');

const recipient_number = 918088896456;
var message = 'This is a test message to check for nodejs messaging';

const nexmo = new Nexmo({
  apiKey: '0ea83234',
  apiSecret: '9a14ec09a4714574'
}, {debug: true});


nexmo.message.sendSms('FromMedicento', recipient_number, message, { type: 'unicode' },
    (err, responseData) => {
      if(err) {
        console.log(err);
      } else {
        console.dir(responseData);
        // Get data from response
        const data = {
          id: responseData.messages[0]['message-id'],
          number: responseData.messages[0]['to']
        }


      }
    }
  );
