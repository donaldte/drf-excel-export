import logging
from openpyxl import Workbook

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Try to import drf-spectacular
try:
    from drf_spectacular.openapi import AutoSchema as SpectacularSchema
    spectacular_available = True
except ImportError:
    spectacular_available = False

# Try to import drf-yasg
try:
    from drf_yasg.openapi import Info, Schema
    from drf_yasg.generators import OpenAPISchemaGenerator
    yasg_available = True
except ImportError:
    yasg_available = False


def generate_api_schema():
    """
    Generates the OpenAPI schema for the DRF API using drf-spectacular or drf-yasg.
    """
    if spectacular_available:
        # If drf-spectacular is installed, use it to generate the schema
        schema = SpectacularSchema()
        logger.info("Using drf-spectacular to generate the schema.")
    elif yasg_available:
        # If drf-yasg is installed, use it to generate the schema
        generator = OpenAPISchemaGenerator(
            info=Info(
                title="API Documentation",
                default_version="v1",
            )
        )
        schema = generator.get_schema(request=None, public=True)
        logger.info("Using drf-yasg to generate the schema.")
    else:
        # If neither library is available, raise an error
        logger.error("Neither drf-spectacular nor drf-yasg is installed. Please install one to generate the schema.")
        raise ImportError("Neither drf-spectacular nor drf-yasg is installed. Please install one to generate the schema.")
    
    return schema


def export_to_excel(schema):
    """
    Exports the API schema to an Excel file, compatible with drf-spectacular and drf-yasg.
    """
    # Create a new Excel workbook and set up the main sheet
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "API Documentation"
    
    # Define headers for the Excel file
    headers = ["Endpoint", "Method", "Description", "Parameters", "Response Codes"]
    sheet.append(headers)

    # Extract information based on schema type
    if spectacular_available:
        # drf-spectacular schema handling
        for path, path_item in schema.get_paths().items():
            for method, operation in path_item.items():
                # Extract data for each endpoint
                description = operation.get('description', '')
                parameters = [param['name'] for param in operation.get('parameters', [])]
                responses = list(operation.get('responses', {}).keys())
                
                # Append row to Excel
                sheet.append([
                    path,
                    method.upper(),
                    description,
                    ", ".join(parameters),
                    ", ".join(responses)
                ])
                
    elif yasg_available:
        # drf-yasg schema handling
        for path, path_item in schema['paths'].items():
            for method, operation in path_item.items():
                # Extract data for each endpoint
                description = operation.get('description', '')
                parameters = [param['name'] for param in operation.get('parameters', [])]
                responses = list(operation.get('responses', {}).keys())
                
                # Append row to Excel
                sheet.append([
                    path,
                    method.upper(),
                    description,
                    ", ".join(parameters),
                    ", ".join(responses)
                ])

    # Save the Excel file
    workbook.save("api_documentation.xlsx")
    logger.info("Export complete: 'api_documentation.xlsx'")
