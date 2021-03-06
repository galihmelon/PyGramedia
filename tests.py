import asyncio
import unittest

from aioresponses import aioresponses

from pygramed import PyGramedia


class PyGramediaTest(unittest.TestCase):

    def setUp(self):
        self.pg = PyGramedia()

    def test_repr_product(self):
        self.assertEqual(str(self.pg.product), '<ProductAPI: https://www.gramedia.com/api/products/>')

    def test_repr_category(self):
        self.assertEqual(str(self.pg.category), '<CategoryAPI: https://www.gramedia.com/api/categories/>')

    @aioresponses()
    def test_product_retrieve_detail_async(self, mocked=None):
        expected = [{
            "name": "Perpajakan Bendahara Desa",
            "authors": [
                {
                    "title": "M.bahrun Nawawi",
                    "href": "https://www.gramedia.com/api/authors/author-mbahrun-nawawi/"
                }
            ],
            "formats": [
                {
                    "name": "Perpajakan Bendahara Desa",
                    "title": "Soft Cover",
                }
            ],
            "thumbnail": "https://cdn.gramedia.com/uploads/items/9789790625433_perpajakan-bendahara-desa.jpg",
            "href": "https://www.gramedia.com/api/products/perpajakan-bendahara-desa/",
        }]
        loop = asyncio.get_event_loop()
        mocked.get('https://www.gramedia.com/api/products/?per_page=1', payload=list(expected))
        resp = loop.run_until_complete(self.pg.product.retrieve_async(limit=1))
        self.assertIn('perpajakan-bendahara-desa', resp[0].href)

    @aioresponses()
    def test_product_retrieve_detail(self, mocked=None):
        expected = [{
            "name": "Perpajakan Bendahara Desa",
            "authors": [
                {
                    "title": "M.bahrun Nawawi",
                    "href": "https://www.gramedia.com/api/authors/author-mbahrun-nawawi/"
                }
            ],
            "formats": [
                {
                    "name": "Perpajakan Bendahara Desa",
                    "title": "Soft Cover",
                    "images": [
                        "https://cdn.gramedia.com/uploads/images/207998594_STANDARD-BLIVE-NO.jpg",
                        "https://cdn.gramedia.com/uploads/images/207998594_2_STANDARD-BLIVE-.jpg"
                    ],
                }
            ],
            "thumbnail": "https://cdn.gramedia.com/uploads/items/9789790625433_perpajakan-bendahara-desa.jpg",
            "href": "https://www.gramedia.com/api/products/perpajakan-bendahara-desa/",
        }]
        mocked.get('https://www.gramedia.com/api/products/?per_page=1', payload=list(expected))
        resp = self.pg.product.retrieve(limit=1)
        self.assertIn('perpajakan-bendahara-desa', resp[0].href)
        self.assertEqual(str(resp[0].formats[0].images[0]),
                         "https://cdn.gramedia.com/uploads/images/207998594_STANDARD-BLIVE-NO.jpg")


if __name__ == '__main__':
    unittest.main()
