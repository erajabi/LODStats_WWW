from rdfstats.tests import *

class TestStatResultsController(TestController):

    def test_index(self):
        response = self.app.get(url('stat_results'))
        # Test response...

    def test_index_as_xml(self):
        response = self.app.get(url('formatted_stat_results', format='xml'))

    def test_create(self):
        response = self.app.post(url('stat_results'))

    def test_new(self):
        response = self.app.get(url('new_stat_result'))

    def test_new_as_xml(self):
        response = self.app.get(url('formatted_new_stat_result', format='xml'))

    def test_update(self):
        response = self.app.put(url('stat_result', id=1))

    def test_update_browser_fakeout(self):
        response = self.app.post(url('stat_result', id=1), params=dict(_method='put'))

    def test_delete(self):
        response = self.app.delete(url('stat_result', id=1))

    def test_delete_browser_fakeout(self):
        response = self.app.post(url('stat_result', id=1), params=dict(_method='delete'))

    def test_show(self):
        response = self.app.get(url('stat_result', id=1))

    def test_show_as_xml(self):
        response = self.app.get(url('formatted_stat_result', id=1, format='xml'))

    def test_edit(self):
        response = self.app.get(url('edit_stat_result', id=1))

    def test_edit_as_xml(self):
        response = self.app.get(url('formatted_edit_stat_result', id=1, format='xml'))
