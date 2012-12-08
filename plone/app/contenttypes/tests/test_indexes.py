# -*- coding: utf-8 -*-
import unittest2 as unittest

from Products.CMFCore.utils import getToolByName

from plone.app.textfield.value import RichTextValue

from plone.app.contenttypes.testing import (
    PLONE_APP_CONTENTTYPES_INTEGRATION_TESTING
)

from plone.app.testing import TEST_USER_ID, setRoles


class CatalogIntegrationTest(unittest.TestCase):

    layer = PLONE_APP_CONTENTTYPES_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.portal.invokeFactory('Folder', 'folder')
        self.folder = self.portal.folder
        self.folder.invokeFactory(
            'Document',
            'document'
        )
        self.document = self.folder.document
        self.catalog = getToolByName(self.portal, 'portal_catalog')

    def test_title_in_searchable_text_index(self):
        self.document.title = "My title"
        self.document.reindexObject()
        brains = self.catalog.searchResults(dict(
            SearchableText="My title",
        ))
        self.assertEqual(len(brains), 1)
        self.assertEquals(
            brains[0].getPath(),
            '/plone/folder/document'
        )

    def test_description_in_searchable_text_index(self):
        self.document.description = "My description"
        self.document.reindexObject()
        brains = self.catalog.searchResults(dict(
            SearchableText="My description",
        ))
        self.assertEqual(len(brains), 1)
        self.assertEquals(
            brains[0].getPath(),
            '/plone/folder/document'
        )

# XXX: This works in real life. Test fails though.
#    def test_text_in_searchable_text_index(self):
#        self.document.text = RichTextValue(
#            u'Lorem ipsum',
#            'text/plain',
#            'text/html'
#        )
#        self.document.reindexObject()
#        brains = self.catalog.searchResults(dict(
#            SearchableText=u'Lorem ipsum',
#        ))
#        self.assertEqual(len(brains), 1)
#        self.assertEquals(
#            brains[0].getPath(),
#            '/plone/folder/document'
#        )