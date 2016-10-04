import os
import server
import unittest
import tempfile

from flask import json, jsonify


class TestCase(unittest.TestCase):

    def setUp(self):
        # self.db_fd, server.app.config['DATABASE'] = tempfile.mkstemp()
        server.app.config['TESTING'] = True
        self.app = server.app.test_client()
        # with server.app.app_context():
        #     server.init_db()

    # def tearDown(self):
    #     # os.close(self.db_fd)
    #     os.unlink(server.app.config['DATABASE'])

    def test_get_alarm(self):
        resp = self.app.get('/alarms/ian', follow_redirects=True)
        data = json.loads(resp.data)
        self.assertEquals(data['time'], u'1:23')

    def test_set_alarm(self):
        return self.app.post(
            '/alarms',
            data='username=ian&time=1:23',
            follow_redirects=True,
            content_type='application/json'
        )



if __name__ == '__main__':
    unittest.main()