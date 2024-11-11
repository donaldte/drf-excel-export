import pytest
from unittest import mock
from django.conf import settings
from django import setup

# Minimal configuration to run tests with DRF dependencies
if not settings.configured:
    settings.configure(
        INSTALLED_APPS=[
            "rest_framework",
            "drf_yasg",            # if testing with drf-yasg
            "drf_spectacular",     # if testing with drf-spectacular
        ],
        REST_FRAMEWORK={},
    )
    setup()

from drf_excel_export.export import generate_api_schema, export_to_excel

def test_generate_schema_with_spectacular():
    # Mock drf-spectacular import and check schema generation
    with mock.patch("drf_excel_export.export.SpectacularSchema") as mock_spectacular:
        mock_spectacular.return_value = "Spectacular Schema"
        
        schema = generate_api_schema()
        
        assert schema == "Spectacular Schema", "Failed to generate schema with drf-spectacular"

def test_generate_schema_with_yasg():
    # Mock drf-yasg import and check schema generation
    with mock.patch("drf_excel_export.export.spectacular_available", False):  # Disable drf-spectacular
        with mock.patch("drf_excel_export.export.yasg_available", True):      # Enable drf-yasg
            with mock.patch("drf_excel_export.export.OpenAPISchemaGenerator") as mock_yasg:
                mock_yasg.return_value.get_schema.return_value = "YASG Schema"
                
                schema = generate_api_schema()
                
                assert schema == "YASG Schema", "Failed to generate schema with drf-yasg"

def test_export_to_excel_spectacular():
    # Mock a schema for drf-spectacular and test export to Excel
    schema = "Mock Spectacular Schema"
    
    export_to_excel(schema)
    # Check if the file is created and contains expected content
    # You may add file existence and content verification here if needed

def test_export_to_excel_yasg():
    # Mock a schema for drf-yasg and test export to Excel
    schema = "Mock YASG Schema"
    
    export_to_excel(schema)
    # Check if the file is created and contains expected content
    # You may add file existence and content verification here if needed
