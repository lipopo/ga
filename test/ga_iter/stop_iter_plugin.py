from unittest import TestCase

from ga_iter.stop_iter_plugin import StopIterPlugin


class StopIterPluginTestCase(TestCase):

    def setUp(self):
        self.stop_iter_plugin = StopIterPlugin(100)

    def testPlugin(self):
        self.assertEqual(
            self.stop_iter_plugin.max_iter_count, 100
        )

        try:
            for i in range(100):
                self.stop_iter_plugin.iter_next()
        except Exception as e:
            self.assertIsInstance(e, StopIteration)
